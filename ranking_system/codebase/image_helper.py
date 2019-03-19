# for resize img
import cv2
# for basic load/save
import os

class Helper:
    '''
    for resiuzing image for imagenet
        fixing path to dynamic directory
    '''
    def __init__(self, images, dataset_path):
        self.dataset_path = dataset_path
        self.images = images
        print('init helper')

    def resize(self, images, dim=(224,224)):
        for image in self.images:
            print(image)
            img = cv2.imread(image, cv2.IMREAD_UNCHANGED) 
            print('Original Dimensions : ',img.shape) 
            resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            cv2.imwrite(image, resized) 
            img = cv2.imread(image, cv2.IMREAD_UNCHANGED) 
            print('resized Dimensions : ',img.shape)

    def fix_path(self):
        '''
        return formated path as np.array
        '''
        full_paths = list()
        for img in self.images:
            full_paths.append(self.dataset_path + img)
        self.images = full_paths
        return self.images

if __name__ == "__main__":
    Helper.init()
