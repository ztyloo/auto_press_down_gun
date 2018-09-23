import os
import time
import cv2
import numpy as np
import yaml
from PIL import ImageGrab
from pykeyboard import PyKeyboardEvent
from pymouse import PyMouseEvent

from tab_detection.tab_listener import Tab_Listener
from tab_detection.utils import get_pos


class Tab:
    def __init__(self):
        self.yml = yaml.load(open("tab_position.yaml"))
        self.tab_dict = dict()
        self.png_dict = dict()
        self._fill_png_dict()
        self.tab_listener = Tab_Listener(self.tab_down_func)

    def _fill_png_dict(self):
        for k, v in self.yml.items():
            png_dir = os.path.join('pos', k)
            if os.path.exists(png_dir):  # weapon/scope/...
                tmp_dict = dict()
                for png_name in os.listdir(png_dir):   # png name
                    png_path = os.path.join(png_dir, png_name)
                    gun_name = png_name[:-4]
                    png = cv2.imread(png_path, cv2.IMREAD_UNCHANGED)
                    tmp_dict[gun_name] = png
                    self.png_dict[k] = tmp_dict

    def get_pos_im(self, pos: str):
        im = self.now_screen
        yml = self.yml
        x0 = yml[pos]['x0']
        x1 = yml[pos]['x1']
        y0 = yml[pos]['y0']
        y1 = yml[pos]['y1']
        return im[y0: y1, x0: x1, :]

    def detect(self, pos: str):
        test_im = self.get_pos_im(pos)
        for k, v in self.png_dict[pos].items():
            target_im = v[:, :, 0:3]
            shield = v[:, :, [3]]//255

            test_im = test_im*shield
            target_im = target_im*shield
            if np.all(test_im == target_im):
                return k
        return 'none'

    def tab_down_func(self):
        screen = ImageGrab.grab()
        screen = np.array(screen)
        self.now_screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)


t = Tab()
t.tab_down_func()
t.now_screen = cv2.imread('2.png')
t.detect('weapon')
print()