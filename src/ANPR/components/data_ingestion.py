import os, sys
import urllib.request
from src.ANPR.config.configuration import Configuration
from src.ANPR.constants import *
from src.ANPR.entity.config_entity import DataIngestionConfig
from src.ANPR.exception import *
from src.ANPR.logger.log import logging
from src.ANPR.utils.common import read_yaml
import urllib
import gdown
from zipfile import ZipFile, Path

class DataIngestion :
    def __init__(self, data_ingestion_config: DataIngestionConfig) :
        self.data_ingestion_config = data_ingestion_config
    
    def downlaod_data(self) :
        ''''
        Method Name: get_images_from_drive
        Description: This method download the compressed folder from the drive
        '''
        try :
            now = datetime.now()
            timestamp = CURRENT_TIME_STAMP
            prefix = "https://drive.google.com/uc?/export=download&id="
            url_id = self.data_ingestion_config.data_url.split("/")[-2]
            zip_data_url = prefix + url_id
            file_name = "images.zip"
            zip_data_file_name = os.path.join(self.data_ingestion_config.zip_download_dir, file_name)
            gdown.download(zip_data_url,zip_data_file_name)
        except Exception as e :
            raise ANPR_Exceptioon(e,sys) from e
        
    def _get_updated_list_of_file(self, list_zipfile) :
        try :
            ''''
            Method: _get_updated_list_of_file
            Description: This function take zipfile in list format and return a list that check whether their extension suit or not 
            '''
            return [f for f in list_zipfile if f.endswith(".jpeg") or (f.endswith("xml"))]
        except Exception as e :
            raise ANPR_Exceptioon(e,sys) from e
        
    def _preprocess(self, zipfile:ZipFile, f, working_dir) :
        ''''
        Method: _preprocess
        Description: This function extract all images and write into the destination path
        '''
        try :
            target_filepath = os.path.join(working_dir, f)
            
            if not os.path.exists(target_filepath) :
                zipfile.extract(f, working_dir)

            if os.path.getsize(target_filepath == 0) :
                os.remove(target_filepath)

        
        except Exception as e :
            raise ANPR_Exceptioon(e,sys) from e
        
    def get_clean_and_unzipfile(self,zip_file_path: str, unzip_dir_path:str) -> Path :
        '''
        Method: get_clean_and_unzipfile()
        Description: This function return the unzip and clear format file
        '''
        try :
            zip_file_path = os.path.join(self.data_ingestion_config.zip_download_dir,"images.zip")
            with ZipFile(zip_file_path, "r") as zip_ref :
                list_of_file = zip_ref.namelist()
                updated_list_of_file = self._get_updated_list_of_file(list_of_file)
                for file in updated_list_of_file :
                    self._preprocess(zip_ref, file, unzip_dir_path)
            return unzip_dir_path
        
    
            
        except Exception as e:
            raise ANPR_Exceptioon(e,sys) from e
        

    def initiate_data_ingestion(self) :
        try :
            #Create data ingestion artifact directory
            os.makedirs(self.data_ingestion_config.zip_download_dir)
            self.downlaod_data()
            self.get_clean_and_unzipfile(zip_file_path=self.data_ingestion_config.zip_download_dir,
                                         unzip_dir_path=self.data_ingestion_config.raw_data_dir)
            

        except Exception as e :
            raise ANPR_Exceptioon(e,sys) from e