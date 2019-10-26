import vectorize as vectorize
import cluster as cluster
import image_helper as imagehelper
import db_transform as trans
# get config
import yaml
import datetime

def init():
    tr = trans.Transform()
    photo_urls = tr.main()

    # prepare dataset for cluster
    cfg = yaml.safe_load(open("config.yaml"))
    dataset_path = cfg['dataset_path']
    prepare_images(photo_urls)
    # prepare cluster
    vec = vectorize.Vectors()
    imhelp = imagehelper.Helper(dataset_path)
    predictions = vec.get_all_vectors(imhelp.get_images())
    cl = cluster.Cluster()
    cl.train(predictions)
    cl.save()


def update():
    current_time = datetime.datetime.now()  # use datetime.datetime.utcnow() for UTC time
    ten_minutes_ago = current_time - datetime.timedelta(minutes=10)
    ten_minutes_ago_epoch_ts = round(ten_minutes_ago.timestamp())  # prepared mongo timestamp
    tr = trans.Transform()
    photo_urls = tr.update(ten_minutes_ago_epoch_ts)
    cfg = yaml.safe_load(open("config.yaml"))
    dataset_path = cfg['dataset_path']
    downloaded_paths = prepare_images(photo_urls)
    # retrain cluster
    vec = vectorize.Vectors()
    imhelp = imagehelper.Helper(dataset_path)
    predictions = vec.get_all_vectors(imhelp.get_images())
    cl = cluster.Cluster()
    cl.train(predictions)
    cl.save()

def prepare_images(photo_urls):
    cfg = yaml.safe_load(open("config.yaml"))
    dataset_path = cfg['dataset_path']
    imhelp = imagehelper.Helper(dataset_path)
    downloaded_paths = imhelp.download_images(photo_urls)
    for path in downloaded_paths:
        imhelp.resize(path)
    return downloaded_paths

if __name__ == "__main__":
    init()