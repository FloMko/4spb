import numpy as np
from keras.applications import VGG19
from keras.preprocessing import image
from keras.engine import Model
from keras.applications.vgg19 import preprocess_input
import logging

class Vectors:
    """
    for CNN network
    """
    def __init__(self):
        self.bm = VGG19(weights='imagenet')
        self.path_to_model='/home/flomko/.keras/models/vgg19_weights_tf_dim_ordering_tf_kernels.h5'
        # self.model = Model(inputs=self.bm.input, outputs=self.bm.get_layer('fc1').output)
        self.model = Model(inputs=self.bm.input, outputs=self.bm.output)
        self.model.load_weights(self.path_to_model)

        logging.debug('Model has been initialized')

    def get_all_vectors(self, paths):
        """
        iterate over dataset
        return preprocessed vectors
        """
        predictions=[]
        for img in paths:
            predictions.append(self.get_vector(img))
        return predictions

    def get_vector(self, path):
        """
        get images
        return preprocessed cnn vector
        """
        # read from file
        img = image.load_img(path, target_size=(224, 224))
        # make vector
        x = image.img_to_array(img)
        # transform vector to one-dimension
        x = np.expand_dims(x, axis=0)
        # preprocesing by library
        x = preprocess_input(x)
        vec = self.model.predict(x)
        vec = vec.ravel()
        return vec

    def load_model(self):
        self.model.load_weights(self.path_to_model)
        logging.debug('Model has been load')


    def save_model(self):
        self.model.save_weights(self.path_to_model)
        logging.debug('Model has been saved')

    def download_model(self):
        self.model = Model(inputs=self.bm.input, outputs=self.bm.get_layer('fc1').output)
        logging.debug('Model has been re-download')
        self.save_model()