# for resize img
import cv2

# for basic load/save
import os
import requests
import shutil

# logging
import logging


class Helper:
    """
    for resizing image for image Net
    fixing path to dynamic directory
    """

    def __init__(self, location):
        self.sources = location
        self.images = self.get_images()
        logging.debug("Image helper has been initialized")

    def get_images(self):
        self.images = os.listdir(self.sources)
        paths = []
        for img in self.images:
            paths.append(self.sources + img)
        return paths

    def download_images(self, photo_urls):
        """
        download images
        :return: self.images
        """
        images_paths = []
        for photo_url in photo_urls:
            response = requests.get(photo_url, stream=True)
            path_to_download = self.sources + photo_url.split("/")[-1]
            images_paths.append(path_to_download)
            with open(path_to_download, "wb") as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
        self.images = os.listdir(path=self.sources)
        logging.debug("All photos has been downloaded")
        return images_paths

    @staticmethod
    def resize(path, dim=(224, 224)):
        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imwrite(path, resized)

    def download_image(self, photo_url):
        """
        for download single image
        :param photo_url: what to download
        :return:photo_path
        """
        response = requests.get(photo_url, stream=True)
        path = self.sources + photo_url.split("/")[-1]
        with open(path, "wb") as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        logging.debug(path + " Has been downloaded")
        return path

    @staticmethod
    def remove_image(photo_path):
        os.remove(photo_path)
        logging.debug(photo_path + " Has been removed")
