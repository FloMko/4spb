from sklearn.neighbors import NearestNeighbors
from sklearn.externals import joblib
# get logging
import logging
# get config
import yaml


class Cluster:
    """
    Class for k-Nearest-Neigborhood cluster
    """
    def __init__(self):
        self.knn = NearestNeighbors(metric='cosine', algorithm='brute')
        cfg = yaml.safe_load(open("config.yaml"))
        self.cluster_path = cfg['cluster_path']
        logging.debug('Cluster has been initialized')

    def find_nearest(self, prediction,n_neighbors):
        """
        get vector
        return cluster space, with indices
        """
        dist, indices = self.knn.kneighbors(prediction.reshape(1,-1), n_neighbors)
        return dist, indices

    def get_similar_images(self, images, dist, indices):
        """
        Iterate over list if images, coolocate indices return list with nearests
        """
        similar_images = [(images[indices[0][i]], dist[0][i]) for i in range(len(indices[0]))]
        return similar_images

    def train(self, predictions):
        self.knn.fit(predictions)

    def save(self):
        joblib.dump(self.knn, self.cluster_path, compress=9)

    def load(self):
        self.knn = joblib.load(self.cluster_path)


if __name__ == "__main__":
    Cluster.init()
