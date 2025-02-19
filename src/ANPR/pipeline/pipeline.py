from collections import namedtuple
from datetime import datetime
import uuid
from src.ANPR.config.configuration import Configuration
from src.ANPR.logger.log import logging, get_log_file_name
from src.ANPR.exception import ANPR_Exceptioon
from threading import Thread
from typing import List
from multiprocessing import Process

from src.ANPR.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig, PrepareCallbacksConfig, TrainingConfig, DataTransformationConfig
from ANPR.entity.artifacts_entity import DataIngestionArtifacts, PrepareBaseModelArtifacts, DataTransformationArtifacts
from src.ANPR.constants import EXPERIMENT_DIR_NAME, EXPERIMENT_FILE_NAME
from ANPR.components.data_ingestion import DataIngestion
from ANPR.components.data_transformation import DataTransformation
from ANPR.components.prepare_base_model import PrepareBaseModel
from ANPR.components.model_trainer import ModelTraining

import os ,sys
import pandas as pd

Experiment = namedtuple("Experiment",["experiment_id", "initialization_timestamp", "artifact_time_stamp",
"running_status", "start_time", "stop_time", "execution_time", "message",
"experiment_file_path", "accuracy", "is_model_accepted"])

class Pipeline(Thread) :
    experiment: Experiment = Experiment(*([None]*11))
    experiment_file_path = None

    def __init__(self, config: Configuration) -> None :
        try :
            os.makedirs(config.training_pipeline_config.artifact_dir, exist_ok=True)
            Pipeline.experiment_file_path = os.path.join(config.training_pipeline_config.artifact_dir, EXPERIMENT_DIR_NAME, EXPERIMENT_FILE_NAME)
            super().__init__(daemon=False, name="pipeline")
            self.config = config
            # self.data_ingestion_config = DataIngestionConfig()
            # self.data_transformation_config = DataTransformationConfig()
            # self.prepare_base_model_config = PrepareBaseModelConfig()
            # self.training_config = TrainingConfig()
            # self.prepare_callbacks_config = PrepareCallbacksConfig()
        except Exception as e:
            raise ANPR_Exceptioon(e, sys) from e
    
    def start_data_ingestion(self) -> DataIngestionArtifacts :
        try :
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e :
            raise ANPR_Exceptioon(e,sys) from e
        
    def start_data_transformation(self, data_ingestion_artifact: DataIngestionArtifacts) -> DataTransformation :
        try :
            logging.info("Entered the start_data_transformation method of TrainingPipeline class")
            data_ingestion_obj = DataTransformation(data_transformation_config=self.config.data_transformation_config(),
                                                    data_ingestion_artifacts = self.config.get_data_ingestion_artifacts())
            data_transformation_artifact = data_ingestion_obj.initiate_data_transformation()
            logging.info("Exited the start_data_transformation method of TrainignPipeline Class")
            return data_transformation_artifact
        except Exception as e :
            raise ANPR_Exceptioon(e,sys) from e
        
    def prepare_base_model(self) -> PrepareBaseModelArtifacts :
        try :
            logging.info("Entered the prepare_callbacks method of TrainPipeline Class")
            prepare_base_obj = PrepareBaseModel(
                prepare_base_model_config=self.config.get_prepare_base_model_config())
            prepare_base_model_artifacat = prepare_base_obj.initiate_prepare_base_model()
            return prepare_base_model_artifacat   
        except Exception as e :
            raise ANPR_Exceptioon(e,sys) from e
        
    def model_training(self) :
        try :
            logging.info("Entered the prepare_callbacks method of TrainPipeline class")
            training_boj = ModelTraining(
                training_config=self.config.get_training_config(),
                prepare_callbacks_config=self.config.get_prepare_callbacks_config(),
                data_ingestion_artifact=self.config.get_data_ingestion_artifacts(),
                data_transformation_artifact=self.config.data_transformation_config(),
                prepare_base_model_artifact=self.config.get_prepare_base_model_config()
            )
            model_trainer_artifact = training_boj.initiate_model_training()
            return model_trainer_artifact
        except Exception as e :
            raise ANPR_Exceptioon(e,sys) from e

        
    def run_pipeline(self) :
        try :
            if Pipeline.experiment.running_status:
                logging.info('Pipeline is already running')
                return Pipeline.experiment
            #data ingestion
            logging.info('Pipeline starting.')
            experiment_id = str(uuid.uuid4())
            Pipeline.experiment = Experiment(experiment_id=experiment_id,
                                             initialization_timestamp=self.config.time_stamp,
                                             running_status=True,
                                             start_time=datetime.now(),
                                             stop_time=None,
                                             execution_time=None,
                                             experiment_file_path=Pipeline.experiment_file_path,
                                             is_model_accepted=None,
                                             message='Pipeline has been started',
                                             accuracy=None,
                                             artifact_time_stamp=None)
            logging.info(f'Pipeline experiment: {Pipeline.experiment}')
            self.save_experiment()
            data_ingestion_artifact = self.start_data_ingestion()
            data_transformation_artifact = self.start_data_transformation(data_ingestion_artifact=data_ingestion_artifact)
            prepare_base_model = self.prepare_base_model()
            model_trainer_artifact = self.model_training()
            
            logging.info(f"data_ingestion_start_suggesfully {data_ingestion_artifact}")
            stop_time = datetime.now()
            Pipeline.experiment = Experiment(experiment_id=Pipeline.experiment.experiment_id,
                                             initialization_timestamp=self.config.time_stamp,
                                             running_status=self.config.time_stamp,
                                             start_time=Pipeline.experiment.start_time,
                                             stop_time=stop_time,
                                             execution_time=stop_time - Pipeline.experiment.start_time,
                                             message="Pipeline has been completed",
                                             experiment_file_path=Pipeline.experiment_file_path,
                                             is_model_accepted= None,
                                             accuracy=None,
                                             artifact_time_stamp=None
                                             )
            logging.info(f"Pipeline Experiment: {Pipeline.experiment}")
            self.save_experiment()
        except Exception as e :
            raise ANPR_Exceptioon(e,sys) from e
        
    def run(self) :
        try :
            self.run_pipeline()
        except Exception as e :
            raise ANPR_Exceptioon(e,sys) from e
        
    def save_experiment(self) :
        try :
            if Pipeline.experiment.experiment_id is not None :
                experiment = Pipeline.experiment
                experiment_dict = experiment._asdict()
                experiment_dict: dict = {key: [value] for key, value in experiment_dict.items()}
                experiment_dict.update({
                    "created_time_stamp": [datetime.now()],
                    "experiment_file_path": [os.path.basename(Pipeline.experiment.experiment_file_path)]
                })

                experiment_report = pd.DataFrame(experiment_dict)
                os.makedirs(os.path.dirname(Pipeline.experiment_file_path), exist_ok=True)
                if os.path.exists(Pipeline.experiment_file_path):
                    experiment_report.to_csv(Pipeline.experiment_file_path, index=False, header=False, mode= 'a')
                else :
                    experiment_report.to_csv(Pipeline.experiment_file_path, mode='w', index=False,header=True)
            else :
                print("First start experiment")

        except Exception as e :
            raise ANPR_Exceptioon(e,sys) from e
        
    @classmethod
    def get_experiments_status(cls, limit:int = 5) -> pd.DataFrame :
        try :
            if os.path.exists(Pipeline.experiment_file_path) :
                df = pd.read_csv(Pipeline.experiment_file_path)
                limit = -1 * int(limit)
                return df[limit:].drop(columns=['experiment_file_path', 'initialization_timestamp'], axis=1)
            else :
                return pd.DataFrame
            logging.info(pd.DataFrame) 
        except Exception as e :
            raise ANPR_Exceptioon(e,sys) from e


