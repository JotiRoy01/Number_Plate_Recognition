import pandas as pd
import numpy as np
import cv2
import xml.etree.ElementTree as ET
from ANPR.entity.config_entity import *
from ANPR.entity.artifacts_entity import *
from ANPR.exception import ANPR_Exceptioon
from ANPR.constants import *
from glob import glob
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import os,sys
from ANPR.utils.common import save_numpy_array_data



class DataTransformation :
    def __init__(self, data_transformation_config: DataTransformationConfig, data_ingestion_artifacts:DataIngestionArtifacts):
        self.data_transformation_config = data_transformation_config
        self.data_ingestion_artifacts = data_ingestion_artifacts
    
    def get_bounding_box_coordinates(self) :
        '''
        Method Name: get_bounding_box_coordinates
        Description: This method will indivisually take each file and parse into xml.etree and find the object and find boundrybox object.
        Then we extract xmin,xmax,ymin,ymax and save those values in the dictionary named labels_dict.
        '''
        try :
            path = glob(os.path.join(self.data_ingestion_artifacts.image_data_dir,"*.xml"))
            labels_dict = dict(filepath=[],xmin=[],xmax=[],ymin=[],ymax=[])
            for filename in path :
                tree = ET.parse(filename)
                root = tree.getroot()
                member_object = root.find("object")
                labels_info = member_object.find("bndbox")
                xmin = int(labels_info.find("xmin").text)
                xmax = int(labels_info.find("xmax").text)
                ymin = int(labels_info.find("ymin").text)
                ymax = int(labels_info.find("ymax").text)

                labels_dict["filepath"].append(filename)
                labels_dict["xmin"].append(xmin)
                labels_dict["xmax"].append(xmax)
                labels_dict["ymin"].append(ymin)
                labels_dict["ymax"].append(ymax)
                dataframe = pd.DataFrame(labels_dict)
                dataframe.to_csv(self.data_transformation_config.labeled_dataframe,index=False)
                return dataframe
        except Exception as e :
            raise ANPR_Exceptioon(e,sys) from e

    def data_preprocessing(self,labels_dataframe, images_path_list) :
        '''
        Method Name: data_preprocessing
        Description: In this method we will first normalization our data &
        we will resize image into (224,224) because it is the standard compatible size of pre trained transfer learning model ie. Inception Resnet V2
        '''
        try :
            labels = labels_dataframe.iloc[:,1:].values
            data = []
            output = []
            for index in range(len(images_path_list)) :
                image = images_path_list[index]
                image_array = cv2.imread(image)
                height,width,depth = image_array.shape
                
                load_image = load_img(image, target_size = (224,224))
                load_image_array = img_to_array(load_image)
                #we wil normalize the image by dividing with maxium number ie. 255(max no for 8 bi images) and the process is call normalization(Min-Max Scaler)
                normalize_load_image_arr = load_image_array/255.0

                xmin,xmax,ymin,ymax = labels[index]
                normalized_xmin, normalized_xmax = xmin/width, xmax/width
                normalized_ymin, normalized_ymax = ymin/height, ymax/height
                label_normalized = (normalized_xmin, normalized_xmax, normalized_ymin, normalized_ymax)
                data.append(normalize_load_image_arr)
                output.append(label_normalized)
                return data , output
        except Exception as e :
            raise ANPR_Exceptioon(e,sys) from e

    def get_filename_from_XML(self, filename) :
        '''
        Method Name: get_filename_from_XML
        Description: This Method will extract the repective image filename of the XML file 
        '''
        try :
            image_file_name = ET.parse(filename).getroot().find('filename').text
            image_filepath = os.path.join(self.data_ingestion_artifacts.image_data_dir,image_file_name)
            return image_filepath
        except Exception as e :
            raise ANPR_Exceptioon(e,sys) from e

    def initiate_data_transformation(self) : 
        try :
            os.makedirs(self.data_transformation_config.data_transformation_artifact_dir, exist_ok=True)

            labels_dataframe = self.get_bounding_box_coordinates()
            image_path_list = list(labels_dataframe['filepath'].apply(self.get_filename_from_XML))
            data, output = self.data_preprocessing(labels_dataframe, image_path_list)

            # Generating X and y variables
            X = np.array(data, dtype=np.float32)
            y = np.array(output, dtype=np.float32)

            #Save Numpy Array
            save_numpy_array_data(file_path=self.data_transformation_config.transformed_data, array=X)
            save_numpy_array_data(file_path=self.data_transformation_config.transfromed_output,array=y)

            data_transformation_artifact = DataTransformationArtifacts(transformed_data_file_path=self.data_transformation_config.transformed_data,
                                                                       transformed_output_file_path=self.data_transformation_config.transfromed_output)
            return data_transformation_artifact
        except Exception as e :
            raise ANPR_Exceptioon(e,sys) from e 
