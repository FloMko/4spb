from glob import glob

import numpy as np
import scipy.sparse as sp
from keras.applications.vgg19 import preprocess_input
from keras.preprocessing import image



class Transforms:

    def __init__(self, images, model):
        self.images = images
        self.model = model

    def vectorize_all(self, px=224, n_dims=512, batch_size=218):
        print("Will vectorize")
        min_idx = 0
        max_idx = min_idx + batch_size
        total_max = len(self.images)
        preds = sp.lil_matrix((len(self.images), n_dims))

        print("Total: {}".format(self.images))
        while min_idx < total_max - 1:
            print(min_idx)
            X = np.zeros(((max_idx - min_idx), px, px, 3))
            # For each file in batch, 
            # load as row into X
            i = 0
            for i in range(min_idx, max_idx):
                file = self.images[i]
                try:
                    img = image.load_img(file, target_size=(px, px))
                    img_array = image.img_to_array(img)
                    X[i - min_idx, :, :, :] = img_array
                except Exception as e:
                    print(e)
            max_idx = i
            X = preprocess_input(X)
            these_preds = self.model.predict(X)
            shp = ((max_idx - min_idx) + 1, n_dims)
            preds[min_idx:max_idx + 1, :] = these_preds.reshape(shp)
            min_idx = max_idx
            max_idx = np.min((max_idx + batch_size, total_max))
        return preds

