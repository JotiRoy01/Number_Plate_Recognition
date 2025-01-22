from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig",
                                 ["data_url","zip_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir","ingested_dir"])
TrainingPipelineConfig = namedtuple("TrainingPipelineConfig",["artifact_dir"])