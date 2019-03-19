import os

import ranking_system.codebase.image_helper as imageHelper
dataset_path='./ranking_system/dataset/'
images = os.listdir(path=dataset_path)
images = imageHelper.Helper(images,dataset_path).fix_path()

import ranking_system.codebase.cluster as cluster

cl =  cluster.Cluster(images)

import ranking_system.codebase.vectorize as vectorize 

tr = vectorize.Transforms(images, cl.model)


#WIP!
# cause error tr.vectorize_all
# cannot reshape array of size 892928 into shape (218,512)
tr.vectorize_all