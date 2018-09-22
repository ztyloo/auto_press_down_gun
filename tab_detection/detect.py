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
        self.fill_png_dict()
        self.tab_listener = Tab_Listener(self.tab_down_func)

    def fill_png_dict(self):
        for k, v in self.yml.items():
            png_dir = v['dir']
            if png_dir is not None:
                for png_name in png_dir:
                    tmp_dict = dict()
                    self.png_dict[k+'_png'] = cv2.imread(png_name)

    def get_pos_im(self, pos: str):
        im = self.now_screen
        yml = self.yml
        x0 = yml[pos]['x0']
        x1 = yml[pos]['x1']
        y0 = yml[pos]['y0']
        y1 = yml[pos]['y1']
        return im[y0: y1, x0: x1, :]

    def detect_pos_im(self, pos: str):
        self.png_dict[]

    def tab_down_func(self):
        screen = ImageGrab.grab()
        screen = np.array(screen)
        self.now_screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)

