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



###
knn.fit(predictions)
dist, indices = knn.kneighbors(predictions[21].reshape(1,-1), n_neighbors=218)
similar_images = [(images[indices[0][i]], dist[0][i]) for i in range(len(indices[0]))]
# it'l return simular ~0.2 deA3A6leeZ0.jpg & hNhm6fAEs5k.jpg



#WIP!
# cause error tr.vectorize_all
# cannot reshape array of size 892928 into shape (218,512)
tr.vectorize_all