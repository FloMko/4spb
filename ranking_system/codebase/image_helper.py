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
        self.paths = []
        print('init helper')

    def resize(self, dim=(224,224)):
        for image in self.paths:
            print(image)
            img = cv2.imread(image, cv2.IMREAD_UNCHANGED) 
            print('Original Dimensions : ',img.shape) 
            resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            cv2.imwrite(image, resized) 
            img = cv2.imread(image, cv2.IMREAD_UNCHANGED) 
            print('resized Dimensions : ',img.shape)

    def fix_path(self):
        '''
        return formated path, images list
        '''
        for img in self.images:
            self.paths.append(self.dataset_path + img)
        return self.paths

if __name__ == "__main__":
    Helper.init()
