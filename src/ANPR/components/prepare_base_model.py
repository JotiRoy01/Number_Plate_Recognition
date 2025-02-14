from src.ANPR.entity.config_entity import *
from src.ANPR.entity.artifacts_entity import *
from src.ANPR.exception import ANPR_Exceptioon
from src.ANPR.constants import *
import tensorflow as tf
from pathlib import Path
import os, sys


class PrepareBaseModel :
    def __init__(self, prepare_base_model_config: PrepareBaseModelConfig):
        self.prepare_base_model_config = prepare_base_model_config
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
    
    def get_base_model(self) :
        """"
        Method Name: get_base_model
        Description: This method will use the Inception-ResNet-v2 model with pre-trained weights and save it as base model
        """
        self.model = tf.keras.applications.InceptionResNetV2(
            input_shape = IMAGE_SIZE,
            weights = WEIGHTS,
            include_top = INCLUDE_TOP
        )
        base_model_path = Path(self.prepare_base_model_config.base_model_path)
        self.save_model(base_model_path,model=self.model)

    def get_updated_model(self) :
        output_model = self.model.output
        output_model = tf.keras.layers.Flatten()(output_model)
        output_model = tf.keras.layers.Dense(500, activation='relu')(output_model)
        output_model = tf.keras.layers.Dense(250, activation='relu')(output_model)
        output_model = tf.keras.layers.Dense(4, activation= 'sigmoid')(output_model)
        final_model = tf.keras.models.Model(inputs = self.model.input, outputs = output_model)

        final_model.compile(
                optimizer = tf.keras.optimizers.Adam(learning_rate = LEARNING_RATE),
                metrics = ['accuracy'],
                loss = 'mse'

        )
        self.save_model(path = self.prepare_base_model_config.updated_model_path, model=final_model)
        
    def initiate_prepare_base_model(self) :
        try :
            os.makedirs(self.prepare_base_model_config.prepare_base_model_dir,exist_ok=True)
            self.get_base_model()
            self.get_updated_model()
            prepare_base_model_artifact = PrepareBaseModelArtifacts(
                base_model_path= self.prepare_base_model_config.base_model_path,
                updated_model_path= self.prepare_base_model_config.updated_model_path
            )
            return prepare_base_model_artifact
        except Exception as e :
            raise ANPR_Exceptioon(e,sys) from e
            

            