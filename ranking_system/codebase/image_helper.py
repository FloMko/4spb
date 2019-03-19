# for resize img
import cv2
# for basic load/save
import os
dataset_path='./ranking_system/dataset/'
images = os.listdir(path=dataset_path)


def resize(images, image_path, dim=(224,224)):
    for image in images:
        print(image)
        img = cv2.imread(image_path+image, cv2.IMREAD_UNCHANGED) 
        print('Original Dimensions : ',img.shape) 
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        cv2.imwrite(image_path+image, resized) 
        img = cv2.imread(image_path+image, cv2.IMREAD_UNCHANGED) 
        print('resized Dimensions : ',img.shape) 


def main():
    resize(images, dataset_path)

if __name__ == "__main__":
    main()
