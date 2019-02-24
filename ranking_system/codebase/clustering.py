import cv2
import numpy as np
# defining feature extractor that we want to use
from sklearn.cluster import KMeans
import sklearn
import os
from sklearn.neighbors import NearestNeighbors
from sklearn import svm
from sklearn.metrics import accuracy_score


extractor = cv2.xfeatures2d.SIFT_create()

dataset_path = '/dataset'
images = os.listdir(path=dataset)
image_path = '0t8wjdjFbX8.jpg'
sift_keypoints = []
feature_vectors=[]
class_vectors=[]

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

def get_histogram(images, cluster):
    feature_vectors=[]
    class_vectors=[]
    for image in images:
        img = cv2.imread(dataset_path+image)
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, descriptors = features(gray_image, extractor)
        #classification of all descriptors in the model
        predict_kmeans=cluster.predict(descriptors)
        #calculates the histogram
        hist, bin_edges=np.histogram(predict_kmeans,bins=num_cluster)
        #histogram is the feature vector
        feature_vectors.append(hist)
        #define the class of the image (elephant or electric guitar)
        class_vectors.append(str(image))
    feature_vectors=np.asarray(feature_vectors)
    class_vectors=np.asarray(class_vectors)
    #return vectors and classes we want to classify
    return class_vectors, feature_vectors


def main():
    print("Step 1: Calculating Kmeans classifier")
    descriptors = get_descriptors(images)
    print("Step 1.2 Training KMeans")
    cluster = clusterize_descriptor(descriptors)
    print("Step 2: Extracting histograms of training and testing images")
    print("Training")
    [train_class,train_featvec] = get_histogram(images, cluster)
    print("Testing")
    [test_class,test_featvec] = get_histogram(train_images,cluster)
    print("Step 3: Training the SVM classifier")
    clf = svm.SVC()
    clf.fit(train_featvec, train_class)

    print("Step 4: Testing the SVM classifier")  
    predict=clf.predict(test_featvec)

    score=accuracy_score(np.asarray(test_class), predict)

    print("Accuracy:" +str(score))



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