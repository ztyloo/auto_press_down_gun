import os
import time
import cv2
import numpy as np
from utils import Detection


class Fire_Mode_Detector(Detection):
    def __init__(self):
        super().__init__()
        self.png_dir = 'b_detection/sub_im'
        self.item_list = ['burst', 'full', 'single']
        super()._fill_png_dict()

    def detect(self, im, thr=10000):
        area_dict = dict()
        area_max = 0.
        for item_name, png in self.png_dict.items():
            area = im_area_sum(im, png)
            area_dict[item_name] = area
            area_max = max(area_max, area)

        for item_name, area in area_dict.items():
            if area_max == area:
                return item_name


def im_area_sum(im_3c: np.ndarray, im_4c: np.ndarray):
    test_im = im_3c.copy()
    shield = im_4c[:, :, [3]] // 255

    test_im = test_im * shield

    # cv2.imshow('target_im', target_im)
    # cv2.waitKey(2000)
    # cv2.imshow('test_im', test_im)
    # cv2.waitKey(2000)
    # print(np.sum(test_im ))

    return np.sum(test_im)