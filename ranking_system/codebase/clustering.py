import cv2
import numpy as np
# defining feature extractor that we want to use
from sklearn.cluster import KMeans
import sklearn
import os
from sklearn.neighbors import NearestNeighbors


extractor = cv2.xfeatures2d.SIFT_create()

images = os.listdir(path='.')
image_path = '0t8wjdjFbX8.jpg'
sift_keypoints = []

# should be as length of dataset
num_cluster = 268 


def features(image, extractor):
    keypoints, descriptors = extractor.detectAndCompute(image, None)
    return keypoints, descriptors

def get_descriptors(images):
    for image in images:
        img = cv2.imread(image)
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, descriptors = features(gray_image, extractor)
        sift_keypoints.append(descriptors)
    return sift_keypoints



def build_histogram(descriptor_list, cluster_alg):
    histogram = np.zeros(len(cluster_alg.cluster_centers_))
    cluster_result =  cluster_alg.predict(descriptor_list)
    for i in cluster_result:
        histogram[i] += 1.0
    return histogram

def clusterize_descriptor(descriptors):
    # get feature as np.array, return as a clusterezid
    sift_keypoints=np.asarray(descriptors)
    sift_keypoints=np.concatenate(descriptors, axis=0) 
    kmean = sklearn.cluster.MiniBatchKMeans(n_clusters=num_cluster, random_state=0).fit(sift_keypoints)
    return kmean


def main():
    print("Step 1: Calculating Kmeans classifier")
    descriptors = get_descriptors(images)
    print("Step 1.2 Training KMeans")
    model = clusterize_descriptor(descriptors)
    print("That's all")
    print(type(model))
    model.shape



if __name__ == "__main__":
    main()




#     if (descriptor is not None):
#         histogram = build_histogram(descriptor, kmeans)
#         preprocessed_image.append(histogram)


# data = cv2.imread(image_path)
# data = gray(data)
# keypoint, descriptor = features(data, extractor)
# histogram = build_histogram(descriptor, kmeans)
# neighbor = NearestNeighbors(n_neighbors = 20)
# neighbor.fit(preprocess_image)
# dist, result = neighbor.kneighbors([histogram])
# print(dist, result)