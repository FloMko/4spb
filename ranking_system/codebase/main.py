
import vectorize as vectorize
import cluster as cluster


import image_helper as imagehelper
import db_transform as trans

tr = trans.Transform()
photos_url = tr.main()


# prepare dataset for cluster
dataset_path='../dataset/'
imhelp = imagehelper.Helper(photos_url,dataset_path)
imhelp.download_images()
images = imhelp.images
paths = imhelp.fix_path()
for path in paths:
    imhelp.resize(path)

# prepare cluster
vec = vectorize.Vectors(paths)
predictions = vec.get_all_vectors()
cl = cluster.Cluster(predictions)

# how-to find image
dist, indices = cl.find_nearest(predictions[20])
simular_images = cl.get_similar_images(images, dist, indices)


print(simular_images)
# # Help to reload module
# import importlib
# importlib.reload(ranking_system.codebase.cluster)