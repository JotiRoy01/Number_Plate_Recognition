from ANPR.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from ANPR.utils.common import *
from ANPR.logger import log
import os, sys
from ANPR.constants import *
from ANPR.exception import *


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

        