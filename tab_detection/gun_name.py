import os
import cv2

from tab_detection.utils import detect_item_sum


class Gun_Name_Detector():
    def __init__(self):
        self.gun_name_list = ['98k', 'akm', 'aug', 'awm', 'dp28', 'groza', 'm16', 'm24', 'm249', 'm416', 'm762',
                              'mini14', 'mk14', 'mk47', 'qbu', 'qbz', 's12k', 's1987', 's686', 'scar', 'sks', 'slr',
                              'tommy', 'ump9', 'uzi', 'vector', 'vss', 'win94']
        self.png_dir = ''
        self.gun_png_dict = dict()
        self._fill_png_dict()

    def _fill_png_dict(self):
        for gun_name in self.gun_name_list:
            gun_png_name = gun_name+'.png'
            gun_png_path = os.path.join(self.png_dir, gun_png_name)
            if os.path.exists(gun_png_path):
                png = cv2.imread(gun_png_path, cv2.IMREAD_UNCHANGED)
                self.gun_png_dict[gun_name] = png

    def detect(self, im):
        for gun_name, png in self.gun_png_dict.items():
            if detect_item_sum(im, png) < 10:
                return gun_name
        return 'none'

