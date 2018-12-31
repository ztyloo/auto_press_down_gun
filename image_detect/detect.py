import numpy as np
import cv2
import os
from image_detect.crop_position import position


class Detector:
    def __init__(self, position_name, category_name, thr=10000):
        self.thr = thr

        assert position_name in position
        crop_position = position[position_name]
        self.x0, self.x1, self.y0, self.y1 = crop_position['x0'], crop_position['x1'], crop_position['y0'], crop_position['y1']
        self.png_dict = dict()

        png_dir = os.path.join(os.path.dirname(__file__), category_name)
        assert os.path.exists(png_dir)
        for png_name in os.listdir(png_dir):
            abs_png_name = os.path.join(png_dir, png_name)
            png = cv2.imread(abs_png_name, cv2.IMREAD_UNCHANGED)
            self.png_dict[png_name[:-4]] = png

    def __call__(self, screen):
        crop_im = screen[self.y0: self.y1, self.x0: self.x1, :]
        if self.thr > 0:
            for item_name, png in self.png_dict.items():
                if detect_item_sum(crop_im, png) < self.thr:
                    return item_name
        else:
            min_sum = 10000000
            res = None
            for item_name, png in self.png_dict.items():
                diff_sum = detect_item_sum(crop_im, png)
                if diff_sum < min_sum:
                    min_sum = diff_sum
                    res = item_name
            return res


def detect_item_sum(detect_im_3c: np.ndarray, target_im_4c: np.ndarray):
    test_im = detect_im_3c.copy()
    target_im = target_im_4c[:, :, 0:3]
    shield = target_im_4c[:, :, [3]] // 255

    test_im = test_im * shield
    target_im = target_im * shield

    return np.sum(test_im - target_im)