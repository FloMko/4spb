import numpy as np

from keras.applications import VGG19
from keras.preprocessing import image
from keras.engine import Model
from keras.applications.vgg19 import preprocess_input
import logging
# get config
import yaml

class Vectors:
    """
    for CNN network
    """
    def __init__(self):
        cfg = yaml.safe_load(open("config.yaml"))
        self.vectors_path = cfg['vectors_path']
        self.bm = VGG19(weights='imagenet')
        self.model_path=cfg['model_path']
        self.model = Model(inputs=self.bm.input, outputs=self.bm.get_layer('fc1').output)
        self.preds = np.dtype([('id', 'S15'),('prediction',np.float32,(4096))])
        self.old_vector = None

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

    def get_prediction(self, path):
        """
        process image to CNN vector
        :param path: image to process
        :return: numphy ndarray with [0] - name, [1] CNN vector
        """
        X = np.zeros(1, dtype=self.preds)
        vector = self.get_vector(path)
        id = path.split('/')[-1]
        X['id'] = id
        X['prediction'] = vector
        return X

    def add_vector(self, new_vector):
        """
        for additional operation over vectors
        :param new_vector: get set of predictions, parse them for knn.fit()
        :return: None
        """
        if self.old_vector is None:
            self.old_vector = new_vector
            return self.old_vector
        else:
            self.old_vector = np.vstack((new_vector, self.old_vector))
            return self.old_vector


    def gef_generate(self, X):
        """
        :param X: get set of predictions, parse them for knn.fit()
        :return: None
        """
        onepred = np.empty(4096)
        predictions=[]
        for pred in X:
            print(pred[0][1])
            onepred = vec.add_vector(pred)
            print(len(onepred))
            predictions.append(onepred)
        return predictions

    def save_vectors(self, vectors):
        """
        Let's save vectors to disk
        :param vectors: get np.ndarray,
        :return: None
        """
        np.save(self.vectors_path, vectors)


    def load_vectors(self, ):
        """
        read vectors from disk
        :return: vectors
        """
        return np.load(self.vectors_path)

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
        self.model.load_weights(self.model_path)
        logging.debug('Model has been load')

    def save_model(self):
        self.model.save_weights(self.model_path)
        logging.debug('Model has been saved')

    def download_model(self):
        self.model = Model(inputs=self.bm.input, outputs=self.bm.get_layer('fc1').output)
        logging.debug('Model has been re-download')
        self.save_model()