import os
import vectorize as vectorize
import cluster as cluster
import image_helper as imageHelper



dataset_path='../dataset/'
images = os.listdir(path=dataset_path)



imhelp = imageHelper.Helper(images,dataset_path)
paths = imhelp.fix_path()
imhelp.resize()


vec = vectorize.Vectors(paths)
predictions = vec.get_all_vectors()
cl = cluster.Cluster(predictions) 

dist, indices = cl.find_nearest(predictions[21])
simular_images = cl.get_similar_images(images, dist, indices)


print(simular_images)
# # Help to reload module
# import importlib
# importlib.reload(ranking_system.codebase.cluster)