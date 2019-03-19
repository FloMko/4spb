import os

import ranking_system.codebase.image_helper as imageHelper
dataset_path='./ranking_system/dataset/'
images = os.listdir(path=dataset_path)
images = imageHelper.Helper(images,dataset_path).fix_path()

import ranking_system.codebase.cluster as cluster

cl =  cluster.Cluster(images)


# lets get vector from path
cl.get_vector(cl.path[0])

