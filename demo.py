import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.ANPR.pipeline.pipeline import Pipeline
from src.ANPR.exception import ANPR_Exceptioon
from src.ANPR.logger.log import logging
from src.ANPR.config.configuration import Configuration
from src.ANPR.components.data_ingestion import DataIngestion
from src.ANPR.components.data_transformation import DataTransformation
from src.ANPR.entity.config_entity import DataIngestionConfig
import os
import sys

def main() :
    try :
        config_path = os.path.join("config", "config.yaml")
        pipeline = Pipeline(Configuration(config_file_path=config_path))
        #pipeline.runpipeline()
        #pipeline.start()
        # training_data_config =Configuration(config_file_path=config_path).get_training_pipeline_config()
        # print(training_data_config)
        # logging.info("main function execution completed")
        configure = Configuration(config_file_path=config_path)
        #dataIngestion_config = configure.get_data_ingestion_config()
        #Data_Ingestion
        # data_ingestion_artifacts = configure.get_data_ingestion_artifacts()
        # print(data_ingestion_artifacts)
        data_transformed_artifacts = configure.get_data_transformation_artifact_config()
        print(data_transformed_artifacts)

        data_transformed_config = configure.data_transformation_config()
        data_ingestion_artifacts = configure.get_data_ingestion_artifacts()

        DataTransformation(data_transformed_config,data_ingestion_artifacts).initiate_data_transformation()
        #DataIngestion(dataIngestion_config).initiate_data_ingestion()
        #print(f"{configure.get_prepare_base_model_config()}")  
        #print(f"{configure.get_prepare_callbacks_config()}") 
        #print(f"{configure.get_training_config()}")

    except Exception as e:
        raise ANPR_Exceptioon(e,sys) from e
    
    

if __name__ == "__main__" :
    main()