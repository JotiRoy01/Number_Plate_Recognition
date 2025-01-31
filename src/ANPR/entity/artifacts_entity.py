from collections import namedtuple

DataIngestionArtifacts= namedtuple("DataIngestionArtifacts", ["image_data_dir"])

DataTransformationArtifacts = namedtuple("DataTransformationArtifact", ["transformed_data_file_path", "transformed_output_file_path"])

PrepareBaseModelArtifacts = namedtuple("PrepareBaseModelArtifact", ["base_model_file_path", "updated_model_file_path"])

ModelTrainerArtifacts = namedtuple("ModelTrainerArtifacts", ["trained_model_path"])