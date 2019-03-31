# for resize img
import cv2
# for basic load/save
import os
import requests
import shutil


class Helper:
    """
    for resizing image for imagenet
    fixing path to dynamic directory
    """
    def __init__(self, photo_urls, dataset_path):
        self.dataset_path = dataset_path
        self.photo_urls = photo_urls
        self.images = []
        self.paths = []
        print('init helper')

    def download_images(self):
        """
        download images
        :return: self.images
        """
        for photo_url in self.photo_urls:
            response = requests.get(photo_url, stream=True)
            with open(self.dataset_path + photo_url.split('/')[-1], 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
        self.images = os.listdir(path=self.dataset_path)
        print('Photos downloaded!')

    def resize(self, dim=(224,224)):
        for image in self.paths:
            img = cv2.imread(image, cv2.IMREAD_UNCHANGED)
            resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            cv2.imwrite(image, resized)

    def fix_path(self):
        """
        return formated path, images list
        """
        for img in self.images:
            self.paths.append(self.dataset_path + img)
        return self.paths