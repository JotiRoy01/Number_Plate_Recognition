import os,sys
from datetime import datetime
from pathlib import Path
#from box import ConfixBox
from ANPR.logger.log import logging
from ANPR.exception import ANPR_Exceptioon
import yaml
import dill
import numpy as np




#CURRENT_TIME_STAMP = get_current_time_stamp()

def save_numpy_array_data(file_path: str, array:np.array) :
        ''''
        save numpy array data to file
        file_path: str location of file to save
        array: np.array data to save
        '''
        try :
            dir_path = os.path.dirname(file_path)
            os.makedirs(dir_path,exist_ok=True)
            with open(file_path, 'wb') as file_obj :
                  np.save(file_obj, array)
        except Exception as e :
            raise ANPR_Exceptioon(e,sys) from e
        

def write_yaml_file(file_path:str,data:dict=None) :
        """"
        Create yaml file
        file_path:str
        data: dict
        """
        try :
            os.makedirs(os.path.dirname(file_path), exist_ok= True)
            with open(file_path, "w") as yaml_file :
                  if data is not None :
                        yaml.dump(data, read_yaml)
        except Exception as e :
           raise ANPR_Exceptioon(e, sys) from e

def read_yaml(config_file_path: Path) -> dict :
        ''''
        read yaml file and returns 

        Args:
            path to yaml (str) : path like input

        Raises:
            ValueError: if yaml file empty
            e: empty file
        '''
        try:
              with open(config_file_path) as yaml_file :
                    content = yaml.safe_load(yaml_file)
                    logging.info(f"yaml_file: {config_file_path} loaded successully")
                    return content
        except Exception as e :
              raise ANPR_Exceptioon(e,sys) from e
