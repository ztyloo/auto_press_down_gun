import numpy as np
import cv2
import os
from image_detect.crop_position import position


class Detector:
    def __init__(self, position_name, category_name):

        assert position_name in position
        crop_position = position[position_name]
        self.x0, self.x1, self.y0, self.y1 = crop_position['x0'], crop_position['x1'], crop_position['y0'], crop_position['y1']
        self.png_dict = dict()

        png_dir = os.path.join('D:/github_project/auto_press_down_gun/image_detect/states_4c_im', category_name)
        assert os.path.exists(png_dir)
        for png_name in os.listdir(png_dir):
            abs_png_name = os.path.join(png_dir, png_name)
            png = cv2.imread(abs_png_name, cv2.IMREAD_UNCHANGED)
            self.png_dict[png_name[:-4]] = png

    def diff_sum_classify(self, screen, sum_thr=10000):
        crop_im = screen[self.y0: self.y1, self.x0: self.x1, :]
        for item_name, png in self.png_dict.items():
            if detect_item_sum(crop_im, png) < sum_thr:
                return item_name

    def water_mark_classify(self, screen, sum_thr=10000, c_thr=5):
        crop_im = screen[self.y0: self.y1, self.x0: self.x1, :]
        crop_im_r = crop_im[:, :, 0]
        crop_im_g = crop_im[:, :, 1]
        crop_im_b = crop_im[:, :, 2]
        crop_im_c_mean = (crop_im_r+crop_im_g+crop_im_b)/3
        crop_im_r_diff = abs(crop_im_r - crop_im_c_mean)
        crop_im_g_diff = abs(crop_im_g - crop_im_c_mean)
        crop_im_b_diff = abs(crop_im_b - crop_im_c_mean)
        crop_im_c_diff_mean = (crop_im_r_diff+crop_im_g_diff+crop_im_b_diff)/3
        shield = np.where(crop_im_c_diff_mean <= c_thr, 255, 0).astype(np.uint8)
        crop_im *= shield[:, :, np.newaxis]

        for item_name, png in self.png_dict.items():
            if detect_item_sum(crop_im, png) < sum_thr:
                return item_name


def detect_item_sum(detect_im_3c: np.ndarray, target_im_4c: np.ndarray):
    test_im = detect_im_3c.copy()
    target_im = target_im_4c[:, :, 0:3]
    shield = target_im_4c[:, :, [3]] // 255

    test_im = test_im * shield
    target_im = target_im * shield

    return np.sum(test_im - target_im)
