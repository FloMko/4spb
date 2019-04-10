import numpy as np
from keras.applications import VGG19
from keras.preprocessing import image
from keras.engine import Model
from keras.applications.vgg19 import preprocess_input




class Vectors:
    '''
    for CNN network
    '''
    def __init__(self):
        self.bm = VGG19(weights='imagenet')
        self.model = Model(inputs=self.bm.input, outputs=self.bm.get_layer('fc1').output)
        print("Init model")

    def get_all_vectors(self, paths):
        '''
        iterate over dataset
        return preprocessed vectors
        '''
        predictions=[]
        for img in paths:
            predictions.append(self.get_vector(img))
        return predictions

    def get_vector(self, path):
        '''
        get images
        return preprocessed cnn vector
        '''
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

if __name__ == "__main__":
    Vectors.init()