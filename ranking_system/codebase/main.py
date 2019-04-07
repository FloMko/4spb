
import vectorize as vectorize
import cluster as cluster


import image_helper as imagehelper
import db_transform as trans
import api_server as api_server

tr = trans.Transform()
photos_url = tr.main()

# prepare dataset for cluster


dataset_path='../dataset/'

imhelp = imagehelper.Helper(photos_url,dataset_path)

def prepare_images():
    for image in imhelp.photo_urls:
        imhelp.download_image(image)
    imhelp.fix_path()
    for path in imhelp.paths:
        imhelp.resize(path)

prepare_images()

# prepare cluster
vec = vectorize.Vectors(imhelp.paths)
predictions = vec.get_all_vectors()
cl = cluster.Cluster(predictions)

# how-to find image
dist, indices = cl.find_nearest(predictions[20])
simular_images = cl.get_similar_images(images, dist, indices)


print(simular_images)

api = api_server.Api(cluster = "")
api.app.run(host='0.0.0.0', debug=True)
# # Help to reload module
# import importlib
# importlib.reload(ranking_system.codebase.cluster)