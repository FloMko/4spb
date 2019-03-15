import numpy as np
from keras.applications import VGG19
from keras.applications.vgg19 import preprocess_input
from keras.engine import Model
from keras.preprocessing import image
from sklearn.neighbors import NearestNeighbors

import os


dataset_path='./ranking_system/dataset/'
images = os.listdir(path=dataset_path)

bm = VGG19(weights='imagenet')
model = Model(inputs=bm.input, outputs=bm.get_layer('fc1').output)

def get_vector(path):
    img = image.load_img(path, target_size=(224, 224)) # чтение из файла
    x = image.img_to_array(img)  # сырое изображения в вектор
    x = np.expand_dims(x, axis=0)  # превращаем в вектор-строку (2-dims)
    x = preprocess_input(x) #  библиотечная подготовка изображения
    vec = model.predict(x).ravel()
    return vec

def main():
    vec = get_vector(dataset_path+images[0])
    print(vec)
    print(vec.shape)

if __name__ == "__main__":
    main()
