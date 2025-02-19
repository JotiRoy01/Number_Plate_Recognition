from ANPR.exception import ANPR_Exceptioon
from ANPR.utils.common import *
from pathlib import Path
import tensorflow as tf
from sklearn.model_selection import train_test_split
from ANPR.entity.config_entity import *
from ANPR.entity.artifacts_entity import *
from ANPR.constants import *
import os, sys, time
from ANPR.components.data_transformation import DataTransformation
from keras.utils import custom_object_scope
from ANPR.components.customlayers import CustomScaleLayer  # Import your custom layer
# Ensure eager execution is enabled
tf.config.run_functions_eagerly(True)


class ModelTraining :
    def __init__(self, 
                 training_config: TrainingConfig,
                 prepare_callbacks_config: PrepareCallbacksConfig,
                 data_ingestion_artifact: DataIngestionArtifacts,
                 data_transformation_artifact: DataTransformationConfig,
                 prepare_base_model_artifact: PrepareBaseModelArtifacts) :
        
        self.training_config = training_config
        self.prepare_callbacks_config = prepare_callbacks_config
        self.data_ingestion_artifact = data_ingestion_artifact
        self.data_transformation_artifact = data_transformation_artifact
        self.prepare_base_model_artifact = prepare_base_model_artifact

    @property
    def _create_tb_callbacks(self) :
        timestamp = time.strftime("%Y-%M-%D-%H-%M-%S")
        tb_running_log_dir = os.path.join(self.prepare_callbacks_config.tensorbroad_root_log_dir, f"tb_logs_at{timestamp}")
        return tf.keras.callbacks.TensorBoard(log_dir = tb_running_log_dir)
    
    @property
    def _create_ckpt_callbacks(self) :
        return tf.keras.callbacks.ModelCheckpoint(
            filepath = self.prepare_callbacks_config.checkpoint_model,
            save_best_only = True
        )
    
    def get_tensorboard_checkpoints_callbacks(self) :
        return[
            self._create_tb_callbacks,
            self._create_ckpt_callbacks
        ]
    
    # def get_model(self) :
    #     self.model = tf.keras.models.load_model(self.prepare_base_model_artifact.updated_model_path)

    # def get_model(self):
    #     with custom_object_scope({'CustomScaleLayer': CustomScaleLayer}):
    #         self.model = tf.keras.models.load_model(self.prepare_base_model_artifact.updated_model_path)
    def get_model(self):
        with custom_object_scope({'CustomScaleLayer': CustomScaleLayer, 'mse': tf.keras.losses.MeanSquaredError()}):
            self.model = tf.keras.models.load_model(self.prepare_base_model_artifact.updated_model_path)
            # Re-initialize the optimizer
            self.model.compile(optimizer=tf.keras.optimizers.Adam(), loss='mse')
    
    def split_train_test(self):
        #print(f"data numpy array file = {self.data_transformation_artifact.transformed_data}")
        print(f"length = {len(self.data_transformation_artifact.transformed_data)}")
        X = load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_data)
        y = load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_output)

        print(f"Loaded X shape: {X.shape}")
        print(f"Loaded y shape: {y.shape}")

        # Check if the dataset has more than one sample
        if len(X) > 1:
            # Split the data into training and testing set using sklearn
            x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
        else:
            raise ValueError("The dataset must contain more than one sample to perform train-test split.")

        return x_train, x_test, y_train, y_test
    
    @staticmethod
    def save_model(path:Path, model: tf.keras.Model) :
        model.save(path)
    
    def train(self, x_train,x_test, y_train,y_test,callback_list) :
        self.model.fit(
            x_train,
            y_train,
            batch_size = BATCH_SIZE,
            epochs = EPOCHS,
            validation_data = (x_test, y_test),
            callbacks = callback_list
        )
        self.save_model(path=self.training_config.trained_model, model=self.model)

    def initiate_model_training(self) :
        try :
            print(f"updated_model_path{self.prepare_base_model_artifact.updated_model_path}")
            model_ckpt_dir = os.path.dirname(self.prepare_callbacks_config.checkpoint_model)
            model_dir = os.path.dirname(self.training_config.trained_model)

            callback_list = self.get_tensorboard_checkpoints_callbacks()
            
            create_directories([model_ckpt_dir, self.prepare_callbacks_config.tensorbroad_root_log_dir, self.training_config.model_training_dir, model_dir])

            self.get_model()

            x_train, x_test, y_train, y_test = self.split_train_test()

            self.train(x_train,x_test,y_train,y_test, callback_list=callback_list)
            model_trainer_artifact = ModelTrainerArtifacts(trained_model_path=self.training_config.trained_model)

            return model_trainer_artifact
        except Exception as e :
            raise ANPR_Exceptioon(e,sys) from e