import vectorize as vectorize
import cluster as cluster
import imageHelper as imageHelper
import dbTransform as trans

# get config
import yaml

def init():
    tr = trans.Transform()
    photo_urls = tr.main()

    # prepare dataset for cluster
    cfg = yaml.safe_load(open("config.yaml"))
    dataset_path = cfg["dataset_path"]
    prepare_images(photo_urls)
    # prepare cluster
    vec = vectorize.Vectors()
    imhelp = imageHelper.Helper(dataset_path)
    predictions = vec.get_all_vectors(imhelp.get_images())
    cl = cluster.Cluster()
    cl.train(predictions)
    cl.save()


def update(timestamp):
    tr = trans.Transform()
    photo_urls = tr.update(timestamp)
    cfg = yaml.safe_load(open("config.yaml"))
    dataset_path = cfg["dataset_path"]
    prepare_images(photo_urls)
    # retrain cluster
    vec = vectorize.Vectors()
    imhelp = imageHelper.Helper(dataset_path)
    predictions = vec.get_all_vectors(imhelp.get_images())
    cl = cluster.Cluster()
    cl.train(predictions)
    cl.save()


def prepare_images(photo_urls):
    cfg = yaml.safe_load(open("config.yaml"))
    dataset_path = cfg["dataset_path"]
    imhelp = imageHelper.Helper(dataset_path)
    downloaded_paths = imhelp.download_images(photo_urls)
    for path in downloaded_paths:
        imhelp.resize(path)
    return downloaded_paths


if __name__ == "__main__":
    init()
