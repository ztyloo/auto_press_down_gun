import numpy as np
import cv2
import os


class Detector:
    def __init__(self, crop_position, png_dir):
        self.crop_position = crop_position
        self.png_dict = dict()

        for png_name in os.listdir(png_dir):
            abs_png_name = os.path.join(png_dir, png_name)
            png = cv2.imread(abs_png_name, cv2.IMREAD_UNCHANGED)
            self.png_dict[png_name[:-4]] = png

    def __call__(self, im, thr=10000):
        for item_name, png in self.png_dict.items():
            if detect_item_sum(im, png) < thr:
                return item_name


def detect_item_sum(detect_im_3c: np.ndarray, target_im_4c: np.ndarray):
    test_im = detect_im_3c.copy()
    target_im = target_im_4c[:, :, 0:3]
    shield = target_im_4c[:, :, [3]] // 255

    test_im = test_im * shield
    target_im = target_im * shield

    return np.sum(test_im - target_im)