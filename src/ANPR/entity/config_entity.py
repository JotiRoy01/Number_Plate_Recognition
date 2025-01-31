from collections import namedtuple
from ANPR.constants import *
from dataclasses import dataclass

DataIngestionConfig = namedtuple("DataIngestionConfig",
                                 ["data_url","zip_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir","ingested_dir"])
TrainingPipelineConfig = namedtuple("TrainingPipelineConfig",["artifact_dir"])

DataTransformationConfig = namedtuple("DataTransformationConfig",["data_transformation_artifact_dir","labeled_dataframe","transformed_data","transfromed_output"])

PrepareBaseModelConfig = namedtuple("PrepareBaseModelConfig",["prepare_base_model_dir", "base_model_path", "updated_model_path"])

PrepareCallbacksConfig = namedtuple("PrepareCallbacksConfig",["prepare_callbacks_artifacts_dir", "tensorbroad_root_log_dir", "checkpoint_dir", "checkpoint_model"])

TrainingConfig = namedtuple("TrainingConfig", ["model_training_dir", "trained_model"])

PipelineConfig = namedtuple("PipelineConfig",["static_dir", "predict_sub_dir", "roi_sub_dir", "uplaod_sub_dir", "ocr_sub_dir"])

