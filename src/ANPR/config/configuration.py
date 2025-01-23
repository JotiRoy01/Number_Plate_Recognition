from ANPR.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig,DataTransformationConfig, PrepareBaseModelConfig
from ANPR.utils.common import *
from ANPR.logger import log
import os, sys
from ANPR.constants import *
from ANPR.exception import ANPR_Exceptioon


class Configuration :
    def __init__(self,
                 config_file_path:str = CONFIG_FILE_PATH,
                 current_time_stamp:str = CURRENT_TIME_STAMP)->None:
        try:
            self.config_info = read_yaml(config_file_path=config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_time_stamp
        except Exception as e :
            raise ANPR_Exceptioon(e, sys) from e
        
    def get_data_ingestion_config(self) -> DataIngestionConfig :
        try :
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_ingestion_artifact_dir = os.path.join(artifact_dir,
                                                      DATA_INGESTION_DIR_CONFIG_KEY,
                                                      self.time_stamp)
            #data_ingestion_artifact_dir = os.path.join(data_ingested_artifact_dir,DATA_INGESTION_DIR_CONFIG_KEY)

            data_ingested_config_info = self.config_info[DATA_INGESTION_CONFIG_KEY]
            data_url = data_ingested_config_info[DATA_INGESTION_URL_CONFIG_KEY]
        
            raw_data_dir = os.path.join(data_ingestion_artifact_dir, data_ingested_config_info[DATA_INGESTION_RAW_DATA_DIR_CONFIG_KEY])
            zip_download_dir = os.path.join(data_ingestion_artifact_dir,data_ingested_config_info[DATA_INGESTION_RAW_DATA_DIR_CONFIG_KEY],data_ingested_config_info[DATA_INGESTION_ZIP_DOWLOAD_DIR_CONFIG_KEY])
            ingested_train_dir = os.path.join(data_ingestion_artifact_dir, data_ingested_config_info[DATA_INGESTIONTRAIN_TRAIN_DIR_CONFIG_KEY])

            ingested_test_dir = os.path.join(data_ingestion_artifact_dir, data_ingested_config_info[DATA_INGESTIONTEST_TEST_DIR_CONFIG_KEY])
            ingested_dir_config = DataIngestionConfig(
            data_url=data_url,
            zip_download_dir=zip_download_dir,
            raw_data_dir=raw_data_dir,
            ingested_train_dir=ingested_train_dir,
            ingested_test_dir=ingested_test_dir,
            ingested_dir=data_ingestion_artifact_dir)

            return ingested_dir_config
        except Exception as e :
            raise ANPR_Exceptioon(e,sys) from e
        

    def data_transformation_config(self) -> DataTransformationConfig:
        try :
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_transformation_config_info = self.config_info[DATA_TRANSFORMATION_CONFIG]
            data_transformation_dir_path = os.path.join(artifact_dir,data_transformation_config_info[DATA_TRANSFORMATION_ARTIFACT_DIR])
            data_transformantion_labeled_dataframe_file_path = os.path.join(data_transformation_dir_path,data_transformation_config_info[DATA_TRANSFORMATION_LABELED_DATAFRAME])
            data_transformation_transformed_data_file_path = os.path.join(data_transformation_dir_path, data_transformation_config_info[DATA_TRANSFORMATION_TRANSFORMED_DATA])
            data_transformation_transformed_ouput_file_path = os.path.join(data_transformation_dir_path, data_transformation_config_info[DATA_TRANSFORMATION_TRANSFORMED_OUTPUT])

            transform_dir_config = DataTransformationConfig(
                data_transformation_artifact_dir=data_transformation_dir_path,
                labeled_dataframe=data_transformantion_labeled_dataframe_file_path,
                transformed_data=data_transformation_transformed_data_file_path,
                transfromed_output=data_transformation_transformed_ouput_file_path
            )

            return transform_dir_config

        except Exception as e :
            raise ANPR_Exceptioon(e,sys) from e
        
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig :
        try :
            artifact_dir = self.training_pipeline_config.artifact_dir
            prepare_base_model_config_info = self.config_info[PREPARE_BASE_MODEL_CONFIG]
            prepare_base_model_dir_path = os.path.join(artifact_dir, prepare_base_model_config_info[PREPARE_BASE_MODEL_DIR])
            base_model_path = os.path.join(prepare_base_model_dir_path, prepare_base_model_config_info[PREPARE_BASE_MODEL_PATH])
            updated_base_model_path = os.path.join(prepare_base_model_dir_path, prepare_base_model_config_info[PREPARE_BASE_UPDATED_MODEL_PATH])

            prepare_base_config = PrepareBaseModelConfig(
                prepare_base_model_dir=prepare_base_model_dir_path,
                base_model_path=base_model_path,
                updated_model_path=updated_base_model_path
            )
            return prepare_base_config
        except Exception as e :
            raise ANPR_Exceptioon(e,sys) from e
    

    def get_training_pipeline_config(self) ->TrainingPipelineConfig :
        try :
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,
                                    training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
                                    training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])
            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training pipline config: {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e :
            raise ANPR_Exceptioon(e,sys) from e

        