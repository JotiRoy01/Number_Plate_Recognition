# __init__.py for constants
import os
#from from_root import from_root
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

# data transformation related config key
DATA_TRANSFORMATION_CONFIG = "data_transformation_config"
DATA_TRANSFORMATION_ARTIFACT_DIR = "data_transformation_artifact_dir"
DATA_TRANSFORMATION_LABELED_DATAFRAME = "labeled_dataframe"
DATA_TRANSFORMATION_TRANSFORMED_DATA =  "transformed_data"
DATA_TRANSFORMATION_TRANSFORMED_OUTPUT = "transformed_output"


# prepare base model config
PREPARE_BASE_MODEL_CONFIG = "prepare_base_model_config"
PREPARE_BASE_MODEL_DIR = "prepare_base_model_dir"
PREPARE_BASE_MODEL_PATH = "base_model_path"
PREPARE_BASE_UPDATED_MODEL_PATH = "updated_model_path"
AUGMETATION = True
IMAGE_SIZE = [224, 224, 3]
BATCH_SIZE = 8
INCLUDE_TOP= False
EPOCHS = 1
WEIGHTS = 'imagenet'
LEARNING_RATE = 1e-4
CLASSES = 4


#prepare callback related constants
PREPARE_CALLBACKS_CONFIG = "prepare_callbacks_config"
PREPARE_CALLBACKS_ARTIFACTS_DIR= "prepare_callbacks_artifacts_dir"
PREPARE_TENSORBROAD_ROOT_LOG_DIR = "tensorbroad_root_log_dir"
PREPARE_CHECKPOINT_DIR = "checkpoint_dir"
PREPARE_CHECKPOINT_MODEL = "checkpoint_model"

#model traning related constant
TRAINING_CONFIG = "training_config"
TRAINING_TRAINED_MODEL_DIR = "model_training_dir"
TRAINING_TRAINED_MODEL = "trained_model"

#prediction pipeline related constants
PREDICTED_PIPELINE_CONFIG = "predicted_pipelint_config"
STATIC_DIR = "static_dir"
PREDICTED_SUB_DIR= "predict_sub_dir"
ROI_SUB_DIR = "roi_sub_dir"
UPLOAD_SUB_DIR = "upload_sub_dir"
OCR_SUB_DIR = "ocr_sub_dir"

#Artifacts related config
DATA_INGESTION_ARTIFACTS = "data_ingestion_artifacts"
IMAGE_DATA_DIR = "image_data_dir"

#Data Transformation artifacts config
DATA_TRANSFORMATION_ARTIFACTS_CONFIG = "data_transformation_artifact_config"
TRANSFORMED_DATA_FILE_PATH = "transformed_data_file_path"
TRANSFORMED_OUTPUT_FILE_PATH = "transformed_output_file_path"

# Pre paperbase artifacts related constants
PREPARE_BASE_MODEL_ARTIFACTS = "prepare_base_model_artifact"
BASE_MODEL_FILE_PATH = "base_model_file_path"
UPDATED_MODEL_FILE_PATH = "updated_model_file_path"
#Model trainer artifacts related constants
MODEL_TRAINER_ARTIFACTS = "model_trainer_artifacts"
TRAINED_MODEL_PATH = "trained_model_path"

EXPERIMENT_DIR_NAME="experiment"
EXPERIMENT_FILE_NAME="experiment.csv"
