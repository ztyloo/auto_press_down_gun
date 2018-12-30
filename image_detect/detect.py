import numpy as np
import cv2
import os


class Detector:
    def __init__(self, crop_position, png_dir):
        self.x0, self.x1, self.y0, self.y1 = crop_position['x0'], crop_position['x1'], crop_position['y0'], crop_position['y1']
        self.png_dict = dict()

        for png_name in os.listdir(png_dir):
            abs_png_name = os.path.join(png_dir, png_name)
            png = cv2.imread(abs_png_name, cv2.IMREAD_UNCHANGED)
            self.png_dict[png_name[:-4]] = png

    def __call__(self, screen, thr=10000):
        crop_im = screen[self.y0: self.y1, self.x0: self.x1, :]
        for item_name, png in self.png_dict.items():
            if detect_item_sum(crop_im, png) < thr:
                return item_name


def detect_item_sum(detect_im_3c: np.ndarray, target_im_4c: np.ndarray):
    test_im = detect_im_3c.copy()
    target_im = target_im_4c[:, :, 0:3]
    shield = target_im_4c[:, :, [3]] // 255

    test_im = test_im * shield
    target_im = target_im * shield

    return np.sum(test_im - target_im)