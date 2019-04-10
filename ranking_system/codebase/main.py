import vectorize as vectorize
import cluster as cluster
import image_helper as imagehelper
import db_transform as trans

tr = trans.Transform()
photo_urls = tr.main()

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
cl.train(predictions)
cl.save()
