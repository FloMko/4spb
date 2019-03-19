import numpy as np
from keras.applications import VGG19
from keras.applications.vgg19 import preprocess_input
from keras.engine import Model
from keras.preprocessing import image
from sklearn.neighbors import NearestNeighbors

class Cluster:
    def __init__(self, paths):
        self.bm = VGG19(weights='imagenet')
        self.model = Model(inputs=self.bm.input, outputs=self.bm.get_layer('fc1').output)
        self.paths = paths
        print('Init cluster')



    def get_vector(self, path):
        # read from file
        img = image.load_img(path, target_size=(224, 224))
        # make vector
        x = image.img_to_array(img)
        # transform vector to one-dimension
        x = np.expand_dims(x, axis=0)
        # preprocesing by library
        x = preprocess_input(x)
        vec = self.model.predict(x).ravel()
        return vec

    def copy_data(self, data):
        '''
        get array of images, return copy with additional vector
        '''
        print(data.shape)

if __name__ == "__main__":
    Cluster.init()
