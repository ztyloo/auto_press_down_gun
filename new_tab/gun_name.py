import os
import cv2

from tab_detection.utils import detect_item_sum
from utils import Detection


class Gun_Name_Detector(Detection):
    def __init__(self):
        super().__init__()
        self.png_dir = '../tab_detection/pos/weapon'
        self.item_list = ['98k', 'akm', 'aug', 'awm', 'dp28', 'groza', 'm16', 'm24', 'm249', 'm416', 'm762',
                              'mini14', 'mk14', 'mk47', 'qbu', 'qbz', 's12k', 's1987', 's686', 'scar', 'sks', 'slr',
                              'tommy', 'ump9', 'uzi', 'vector', 'vss', 'win94']
        super()._fill_png_dict()