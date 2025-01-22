from ANPR.pipeline.pipeline import Pipeline
from ANPR.exception import ANPR_Exceptioon
from ANPR.logger.log import logging
from ANPR.config.configuration import Configuration
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
        ingestion_config = Configuration(config_file_path=config_path)
        print(f"ingestion_config{ingestion_config.get_data_ingestion_config()}")   

    except Exception as e:
        raise ANPR_Exceptioon(e,sys) from e
    
    

if __name__ == "__main__" :
    main()