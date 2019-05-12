import vectorize as vectorize
import cluster as cluster
import image_helper as imagehelper
import db_transform as trans
# get config
import yaml

tr = trans.Transform()
photo_urls = tr.main()

# prepare dataset for cluster

cfg = yaml.safe_load(open("config.yaml"))

dataset_path = cfg['dataset_path']

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



##
import image_helper as imagehelper
import vectorize as vectorize
import yaml
cfg = yaml.safe_load(open("config.yaml"))
dataset_path = cfg['dataset_path']
imhelp = imagehelper.Helper(dataset_path)
vec = vectorize.Vectors()
pred1 = vec.get_prediction(imhelp.paths[0])
pred2 = vec.get_prediction(imhelp.paths[1])
X = vec.add_vector(pred1, pred2)
