import numpy as np
from sklearn.neighbors import NearestNeighbors

class Cluster:
    def __init__(self, predictions):
        self.predictions = predictions
        self.knn = NearestNeighbors(metric='cosine', algorithm='brute')
        self.knn.fit(self.predictions)
        print('Init cluster')


    def find_nearest(self, prediction,):
        dist, indices = self.knn.kneighbors(prediction.reshape(1,-1), n_neighbors=218)
        return dist, indices

    def get_similar_images(self, images, dist, indices):
        similar_images = [(images[indices[0][i]], dist[0][i]) for i in range(len(indices[0]))]
        return similar_images


if __name__ == "__main__":
    Cluster.init()
