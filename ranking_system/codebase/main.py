import vectorize as vectorize
import cluster as cluster
import image_helper as imagehelper
import db_transform as trans
import api_server as api_server

tr = trans.Transform()
photos_url = tr.main()

# prepare dataset for cluster


dataset_path='../dataset/'

imhelp = imagehelper.Helper(dataset_path)

def prepare_images():
    imhelp.download_images(photo_urls)
    imhelp.fix_path()
    for path in imhelp.paths:
        imhelp.resize(path)

prepare_images()

# prepare cluster
vec = vectorize.Vectors()
predictions = vec.get_all_vectors(imhelp.paths)
cl = cluster.Cluster()
cl.fit(predictions)
cl.save()







##


import cluster as cluster
import image_helper as imagehelper
import db_transform as trans
import vectorize as vectorize
import db_transform as trans

tr = trans.Transform()
data = tr.get_old_db()
data_new = tr.transform_data(data)
tr.get_photos_urls(data_new)
tr.photos_urls
dataset_path='../dataset/'
imhelp = imagehelper.Helper(tr.photos_urls,dataset_path)
imhelp.images[20]
history
vec = vectorize.Vectors(imhelp.paths)
imhelp.paths
vect = vec.get_vector(imhelp.paths[21])
cl = cluster.Cluster
cl = cluster.Cluster()
cl.knn.kneighbors
cl.knn.kneighbors()
cl.load()
cl.knn.kneighbors()
history
vect = vec.get_vector(imhelp.paths[21])
cl.find_nearest(vect)
dist, indices = cl.find_nearest(vect)
cl.get_similar_images(imagehelper.images)
imhelp.images
cl.get_similar_images(imhelp.images)
cl.get_similar_images(imhelp.images, dist,indices)
near = cl.get_similar_images(imhelp.images, dist,indices)
near[:5]
history

# how-to find image
# dist, indices = cl.find_nearest(predictions[20])
# simular_images = cl.get_similar_images(images, dist, indices)
#
#
# print(simular_images)
#
# api = api_server.Api(cluster = "")
# api.app.run(host='0.0.0.0', debug=True)
# # Help to reload module
# import importlib
# importlib.reload(ranking_system.codebase.cluster)