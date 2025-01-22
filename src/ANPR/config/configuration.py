from ANPR.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
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
            data_ingested_artifact_dir = os.path.join(artifact_dir,
                                                      DATA_INGESTION_DIR_CONFIG_KEY,
                                                      self.time_stamp)
            data_ingested_config = self.config_info[DATA_INGESTION_CONFIG_KEY]
            data_url = data_ingested_config[DATA_INGESTION_URL_CONFIG_KEY]
            raw_data_dir = data_ingested_config[DATA_INGESTION_RAW_DATA_DIR_CONFIG_KEY]
            zip_download_dir = data_ingested_config[DATA_INGESTION_ZIP_DOWLOAD_DIR_CONFIG_KEY]
            ingested_dir = data_ingested_config[DATA_INGESTION_DIR_CONFIG_KEY]
            ingested_train_dir = data_ingested_config[DATA_INGESTIONTRAIN_TRAIN_DIR_CONFIG_KEY]
            ingested_test_dir = data_ingested_config[DATA_INGESTIONTEST_TEST_DIR_CONFIG_KEY]
            ingested_dir_config = DataIngestionConfig(
                data_url=data_url,
                zip_download_dir=zip_download_dir,
                raw_data_dir=raw_data_dir,
                ingested_train_dir=ingested_train_dir,
                ingested_test_dir=ingested_test_dir,
                ingested_dir=ingested_dir

        )
            #print(f"data_ingestion_config{data_ingested_config}")
            #print(data_ingestion_artifact_dir)
            logging.info(f"Data ingestion config : {data_ingested_config}")
            return ingested_dir_config
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

        