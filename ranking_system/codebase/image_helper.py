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
        self.fix_path()
        print('init helper')

    def get_images(self):
            self.images = os.listdir(self.dataset_path)

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

    def resize(self, path, dim=(224,224)):
        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        cv2.imwrite(path, resized)

    def fix_path(self):
        """
        help fix paths for all images in dataset_path
        """
        self.get_images()
        for img in self.images:
            self.paths.append(self.dataset_path + img)

    def download_image(self, photo_url):
        """
        for download single image
        :param photo_url: what to download
        :return:photo_path
        """
        response = requests.get(photo_url, stream=True)
        path = self.dataset_path + photo_url.split('/')[-1]
        with open(path, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        print(path+ ' Have been download')

    def remove_image(self, photo_path):
        os.remove(photo_path)
