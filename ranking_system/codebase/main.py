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
import cluster as cluster
import yaml
cfg = yaml.safe_load(open("config.yaml"))
dataset_path = cfg['dataset_path']
imhelp = imagehelper.Helper(dataset_path)
vec = vectorize.Vectors()

predictions=[]
for img in imhelp.paths:
    predictions.append(vec.get_prediction(img))

X = vec.add_vector(predictions[1][0], predictions[0][0])

preds= None
for vector in predictions:
    preds = vec.add_vector(vector[0])


def add_vector(new_vector, old_vector=None):
        '''
        :param vectors: get set of predictions, parse them for knn.fit()
        :return: None
        '''
        if old_vector is None:
            return new_vector
        else:
            old_vector =  np.vstack((new_vector, old_vector))
            return old_vector


cl = cluster.Cluster()
cl.train(predictions)
cl.save()