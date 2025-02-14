import tensorflow as tf
from tensorflow.keras.layers import Layer

class CustomScaleLayer(Layer):
    def __init__(self, scale=1.0, **kwargs):
        super(CustomScaleLayer, self).__init__(**kwargs)
        self.scale = scale

    def call(self, inputs):
        if isinstance(inputs, list):
            return [input_tensor * self.scale for input_tensor in inputs]
        else:
            return inputs * self.scale

    def get_config(self):
        config = super(CustomScaleLayer, self).get_config()
        config.update({'scale': self.scale})
        return config