import os
import time
import cv2
import numpy as np
import yaml


class Tab:
    def __init__(self):
        self.yml = yaml.load(open("tab_detection/tab_position.yaml"))
        # self.yml = yaml.load(open("tab_position.yaml"))
        self.tab_dict = dict()
        self.png_dict = dict()
        self._fill_png_dict()

        self.gun_name = 'none'
        self.scope_time = 1

    def set_screen(self, screen: np.ndarray):
        self.screen = screen

    def _fill_png_dict(self):
        for k, v in self.yml.items():
            dir = 'tab_detection/pos'
            png_dir = os.path.join(dir, k)
            if os.path.exists(png_dir):  # weapon/scope/...
                tmp_dict = dict()
                for png_name in os.listdir(png_dir):   # png name
                    png_path = os.path.join(png_dir, png_name)
                    gun_name = png_name[:-4]
                    png = cv2.imread(png_path, cv2.IMREAD_UNCHANGED)
                    tmp_dict[gun_name] = png
                    self.png_dict[k] = tmp_dict

    def get_pos_im(self, pos: str):
        im = self.screen
        yml = self.yml
        x0 = yml[pos]['x0']
        x1 = yml[pos]['x1']
        y0 = yml[pos]['y0']
        y1 = yml[pos]['y1']
        return im[y0: y1, x0: x1, :]

    def im_area_sum(self, im_3c: np.ndarray, im_4c: np.ndarray):
        test_im = im_3c.copy()
        target_im = im_4c[:, :, 0:3]
        shield = im_4c[:, :, [3]] // 255

        test_im = test_im * shield
        target_im = target_im * shield

        # cv2.imshow('target_im', target_im)
        # cv2.waitKey(2000)
        # cv2.imshow('test_im', test_im)
        # cv2.waitKey(2000)
        # print(np.sum(test_im - target_im))

        return np.sum(test_im - target_im)

    def detect(self, pos: str):
        test_im = self.get_pos_im(pos)
        if pos[0] == '_':
            pos = pos[1:]
        for k, v in self.png_dict[pos].items():
            if self.im_area_sum(test_im, v) < 5000:
                return k
        return 'none'

    def test(self):
        if self.detect('user') == 'Ryanshuai':
            self.gun_name = self.detect('weapon')
            self.gun_name_ = self.detect('_weapon')
            print(self.gun_name)
            print(self.gun_name_)

            scope = self.detect('scope')
            if scope == 'none':
                self.scope_time = 1
            else:
                self.scope_time = int(scope)
            print(self.scope_time)

            scope_ = self.detect('_scope')
            if scope_ == 'none':
                self.scope_time_ = 1
            else:
                self.scope_time_ = int(scope_)
            print(self.scope_time_)

            return True
        return False




if __name__ == '__main__':
    t = Tab()
    dir = 'pos_from/weapon'
    for im_name in os.listdir(dir):
        im_path = os.path.join(dir, im_name)
        t.now_screen = cv2.imread(im_path)

        t.test()

        # det = t.detect('user')
        # print(det)
        # det = t.detect('weapon')
        # print(det)
        # det = t.detect('scope')
        # print(det)
