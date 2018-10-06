import os

import cv2
import numpy as np
from PIL import ImageGrab
import win32api
import win32con


def get_screen():
    screen = ImageGrab.grab()
    screen = np.array(screen)
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    return screen


def move(x, y):
    try:
        x = int(x)
        y = int(y)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y)
    except:
        print('Move Error')


def detect_item_sum(detect_im_3c: np.ndarray, target_im_4c: np.ndarray):
    test_im = detect_im_3c.copy()
    target_im = target_im_4c[:, :, 0:3]
    shield = target_im_4c[:, :, [3]] // 255

    test_im = test_im * shield
    target_im = target_im * shield
    return np.sum(test_im - target_im)


class Detection:
    def __init__(self):
        self.item_list = []
        self.png_dir = ''
        self.png_dict = dict()
        self._fill_png_dict()

    def _fill_png_dict(self):
        for item_name in self.item_list:
            png_name = item_name+'.png'
            png_path = os.path.join(self.png_dir, png_name)
            if os.path.exists(png_path):
                png = cv2.imread(png_path, cv2.IMREAD_UNCHANGED)
                self.png_dict[item_name] = png

    def detect(self, im):
        for item_name, png in self.png_dict.items():
            if detect_item_sum(im, png) < 10:
                return item_name
        return 'none'
