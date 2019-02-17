import cv2
import numpy as np
# defining feature extractor that we want to use
from sklearn.cluster import KMeans
import os
from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import PCA
import pandas as pd


extractor = cv2.xfeatures2d.SIFT_create()
pca = PCA(n_components=1)

images = os.listdir(path='.')
image_path = '0t8wjdjFbX8.jpg'


descriptor_list = np.empty(0)



def features(image, extractor):
    keypoints, descriptors = extractor.detectAndCompute(image, None)
    return keypoints, descriptors

def get_descriptors(images):
    for image in images:
        img = cv2.imread(image)
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, descriptor = features(gray_image, extractor)
        principalComponents = pca.fit_transform(descriptor)
        np.append(descriptor_list,principalComponents)
    return descriptor_list


## need pca
kmeans = KMeans(n_clusters = 128)
kmeans.fit(descriptor_list)


preprocessed_image = []
for image in images:
    img = cv2.imread(image)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    keypoint, descriptor = features(gray_image, extractor)
    if (descriptor is not None):
        histogram = build_histogram(descriptor, kmeans)
        preprocessed_image.append(histogram)


data = cv2.imread(image_path)
data = gray(data)
keypoint, descriptor = features(data, extractor)
histogram = build_histogram(descriptor, kmeans)
neighbor = NearestNeighbors(n_neighbors = 20)
neighbor.fit(preprocess_image)
dist, result = neighbor.kneighbors([histogram])
print(dist, result)