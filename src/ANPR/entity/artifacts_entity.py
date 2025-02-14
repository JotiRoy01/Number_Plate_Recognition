from collections import namedtuple

DataIngestionArtifacts= namedtuple("DataIngestionArtifacts", ["image_data_dir"])

DataTransformationArtifacts = namedtuple("DataTransformationArtifact", ["transformed_data", "transformed_output"])

PrepareBaseModelArtifacts = namedtuple("PrepareBaseModelArtifact", ["base_model_path", "updated_model_path"])

ModelTrainerArtifacts = namedtuple("ModelTrainerArtifacts", ["trained_model_path"])