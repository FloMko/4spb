import os
import ranking_system.codebase.vectorize as vectorize 
import ranking_system.codebase.cluster as cluster
import ranking_system.codebase.image_helper as imageHelper

dataset_path='./ranking_system/dataset/'
images = os.listdir(path=dataset_path)
imhelp = imageHelper.Helper(images,dataset_path)
paths = imhelp.fix_path()
imhelp.resize()


vec = vectorize.Vectors(paths)
predictions = vec.get_all_vectors()
cl = cluster.Cluster(predictions) 

dist, indices = cl.find_nearest(predictions[21])
simular_images = cl.get_similar_images(images, dist, indices)
