# __init__.py for constants
import os
from datetime import datetime
def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

    
ROOT_DIR = os.getcwd()  #to get current working directory
CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)
CURRENT_TIME_STAMP = get_current_time_stamp()

#Training data pipeline
TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"


#data ingestion related config
DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_URL_CONFIG_KEY = "data_url"
DATA_INGESTION_RAW_DATA_DIR_CONFIG_KEY = "raw_data_dir"
DATA_INGESTION_ZIP_DOWLOAD_DIR_CONFIG_KEY = "zip_download_dir"
DATA_INGESTION_DIR_CONFIG_KEY = "ingested_dir"
DATA_INGESTIONTRAIN_TRAIN_DIR_CONFIG_KEY = "ingested_train_dir"
DATA_INGESTIONTEST_TEST_DIR_CONFIG_KEY = "ingested_test_dir"

EXPERIMENT_DIR_NAME="experiment"
EXPERIMENT_FILE_NAME="experiment.csv"
