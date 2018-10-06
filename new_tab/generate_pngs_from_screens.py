import cv2
import os
import yaml
import numpy as np

from new_tab.tab_utils import get_pos_im


white_list = []
diff_list = []


def get_white_shield(im: np.ndarray):
    im_1 = im.max(axis=-1)
    shield = np.where(im_1 == 255, 255, 0).astype(np.uint8)
    return shield


def get_white_shield_im(im: np.ndarray):
    shield = get_white_shield(im)
    shield_im = np.concatenate((im, shield[:, :, np.newaxis]), axis=-1)
    return shield_im


def get_diff_shield(im0: np.ndarray, im1: np.ndarray):
    shield_ = (np.abs(im0 - im1)).max(axis=-1)
    shield = np.where(shield_ == 0, 255, 0).astype(np.uint8)
    return shield


def get_diff_shield_im(im0: np.ndarray, im1: np.ndarray):
    shield = get_diff_shield(im0, im1)
    shield_im = np.concatenate((im0, shield[:, :, np.newaxis]), axis=-1)
    return shield_im




