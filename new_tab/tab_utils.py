import cv2
import numpy as np
import yaml


def get_pos_im(yml: yaml, im: np.ndarray, pos: str):
    x0 = yml[pos]['x0']
    x1 = yml[pos]['x1']
    y0 = yml[pos]['y0']
    y1 = yml[pos]['y1']
    return im[y0: y1, x0: x1, :]
