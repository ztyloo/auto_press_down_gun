import cv2
import numpy as np
import yaml


def get_pos(yml: yaml, pos: str, im: np.ndarray):
    x0 = yml[pos]['x0']
    x1 = yml[pos]['x1']
    y0 = yml[pos]['y0']
    y1 = yml[pos]['y1']
    return im[y0: y1, x0: x1, :]


import itchat

itchat.login()
itchat.send(u'你好', 'filehelper')