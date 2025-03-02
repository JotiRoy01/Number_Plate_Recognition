import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.ANPR.pipeline.pipeline import Pipeline
from src.ANPR.exception import ANPR_Exceptioon
from src.ANPR.logger.log import logging
from src.ANPR.config.configuration import Configuration
from src.ANPR.components.data_ingestion import DataIngestion
from src.ANPR.components.data_transformation import DataTransformation
from src.ANPR.components.prepare_base_model import PrepareBaseModel
from src.ANPR.entity.config_entity import DataIngestionConfig
from src.ANPR.components.model_trainer import ModelTraining
import os
import sys
from src.ANPR.exception import ANPR_Exceptioon
from src.ANPR.logger import log
from src.ANPR.pipeline.pipeline import Pipeline

def main() :
    try :
        config_path = os.path.join("config", "config.yaml")
        configure = Configuration(config_file_path=config_path)
        pipeline = Pipeline(config=configure)
        pipeline.run()
        #experiment_dataframe = pipeline.get_experiments_status()
        #print(experiment_dataframe)
        #pipeline.runpipeline()
        #pipeline.start()
        # training_data_config =Configuration(config_file_path=config_path).get_training_pipeline_config()
        # print(training_data_config)
        # logging.info("main function execution completed")
        
        #dataIngestion_config = configure.get_data_ingestion_config()
        #Data_Ingestion
        # data_ingestion_artifacts = configure.get_data_ingestion_artifacts()
        # print(data_ingestion_artifacts)
        # data_transformed_artifacts = configure.get_data_transformation_artifact_config()
        # print(data_transformed_artifacts)

        #TrainPileline = Pipeline()

        #data_transformed_config = configure.data_transformation_config()
        #data_ingestion_artifacts = configure.get_data_ingestion_artifacts()
        #prepare_base_model_config = configure.get_prepare_base_model_config()

        #PrepareBaseModel(prepare_base_model_config=prepare_base_model_config).initiate_prepare_base_model()

        #ModelTraining(configure.get_training_config(), configure.get_prepare_callbacks_config(), configure.get_data_ingestion_artifacts(),configure.data_transformation_config(),configure.get_prepare_base_model_config()).initiate_model_training()


        

        #DataTransformation(data_transformed_config,data_ingestion_artifacts).initiate_data_transformation()
        #DataIngestion(dataIngestion_config).initiate_data_ingestion()
        #print(f"{configure.get_prepare_base_model_config()}")  
        #print(f"{configure.get_prepare_callbacks_config()}") 
        #print(f"{configure.get_training_config()}")

    except Exception as e:
        raise ANPR_Exceptioon(e,sys) from e
    
    

if __name__ == "__main__" :
    main()