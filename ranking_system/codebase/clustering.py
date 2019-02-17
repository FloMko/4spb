import cv2
import numpy as np
# defining feature extractor that we want to use
from sklearn.cluster import KMeans
import os
from sklearn.neighbors import NearestNeighbors


extractor = cv2.xfeatures2d.SIFT_create()

images = os.listdir(path='.')
image_path = '0t8wjdjFbX8.jpg'


descriptor_list = []



def features(image, extractor):
    keypoints, descriptors = extractor.detectAndCompute(img, None)
    return keypoints, descriptors

for image in images:
    img = cv2.imread(image)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, descriptor = features(gray_image, extractor)
    descriptor_list.append(descriptor)

print(descriptor_list)

kmeans = KMeans(n_clusters = 800)
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