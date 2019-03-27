import numpy as np
from sklearn.neighbors import NearestNeighbors

class Cluster:
    '''
    Class for k-Nearest-Neigborhood cluster
    '''
    def __init__(self, predictions):
        self.predictions = predictions
        self.knn = NearestNeighbors(metric='cosine', algorithm='brute')
        self.knn.fit(self.predictions)
        print('Init cluster')

    def find_nearest(self, prediction,n_neighbors=218):
        '''
        get vector
        return cluster space, with indices
        '''
        dist, indices = self.knn.kneighbors(prediction.reshape(1,-1), n_neighbors)
        return dist, indices

    def get_similar_images(self, images, dist, indices):
        '''
        Iterate over list if images, coolocate indices return list with nearests
        '''
        similar_images = [(images[indices[0][i]], dist[0][i]) for i in range(len(indices[0]))]
        return similar_images


if __name__ == "__main__":
    Cluster.init()
