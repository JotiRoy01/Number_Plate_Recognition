from collections import namedtuple
from ANPR.constants import *
from dataclasses import dataclass

DataIngestionConfig = namedtuple("DataIngestionConfig",
                                 ["data_url","zip_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir","ingested_dir"])
TrainingPipelineConfig = namedtuple("TrainingPipelineConfig",["artifact_dir"])

DataTransformationConfig = namedtuple("DataTransformationConfig",["data_transformation_artifact_dir","labeled_dataframe","transformed_data","transfromed_output"])

PrepareBaseModelConfig = namedtuple("PrepareBaseModelConfig",["prepare_base_model_dir", "base_model_path", "updated_model_path"])
