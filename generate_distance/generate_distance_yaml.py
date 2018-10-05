import cv2
import os
import sys
import yaml
import numpy as np
from PIL import ImageGrab
from pykeyboard import PyKeyboardEvent, PyKeyboard

from generate_distance.find_point import find_upper
from tab_detection.gun_name import Gun_Name_Detector

gun_name_list = ['98k', 'akm', 'aug', 'awm', 'dp28', 'groza', 'm16', 'm24', 'm249', 'm416', 'm762', 'mini14', 'mk14',
                 'mk47', 'qbu', 'qbz', 's12k', 's1987', 's686', 'scar', 'sks', 'slr', 'tommy', 'ump9', 'uzi', 'vector',
                 'vss', 'win94']

full_mode_gun_list = ['aug', 'dp28', 'groza', 'm16', 'm249', 'm416', 'm762', 'mk14', 'qbu', 'qbz', 'scar', 'slr', 'tommy', 'ump9', 'uzi', 'vector', 'vss']





self.k.press_key(160)
self.k.release_key(160)



class Key_Listener(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)
        self.gun_name_detector = Gun_Name_Detector()

    def tap(self, keycode, character, press):
        if keycode == 9 and not press:  # F11
            gun_name = self.gun_name_detector.detect()

    def f11(self, keycode, character, press):
        if keycode == 122 and press:  # F11
            pass





def detect_bullet_holes():
    k = 0
    res_list = []
    i0, j0 = 1719, 719

    while True:
        screen = ImageGrab.grab()
        screen = np.array(screen)
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)

        i1, j1 = find_upper(screen, (i0, j0))
        if i1==0 and j1==0:
            break
        res_list.append((j0 - j1) / 12)

        screen = cv2.circle(screen, (i1, j1), 5, (0, 0, 255), thickness=20)
        cv2.imwrite(str(k)+'.png', screen)

        i0, j0 = i1, j1
        k += 1

    return res_list


def save_yaml(gun_name: str, distance_list: list):
    with open('gun_distance.yaml', 'w') as dumpfile:
        gun_dis_dict[gun_name] = distance_list
        dumpfile.write(yaml.dump(gun_dis_dict))


k = PyKeyboard()
with open('gun_distance.yaml', 'r') as dumpfile:
    gun_dis_dict = yaml.load(dumpfile)

if gun_dis_dict is None:
    gun_dis_dict = dict()



