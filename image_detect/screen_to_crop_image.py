import cv2
import os
import numpy as np

from image_detect.crop_position import *


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


def get_interval_shield(im: np.ndarray, mid, radius):
    shield = im.copy()
    shield = shield.mean(axis=-1)
    shield = np.where(abs(shield - mid) < radius, 255, 0).astype(np.uint8)
    return shield


def get_interval_shield_im(im: np.ndarray, mid, radius):
    shield = get_interval_shield(im, mid, radius)
    shield_im = np.concatenate((im, shield[:, :, np.newaxis]), axis=-1)
    return shield_im


from_dir = 'screens'
to_dir = 'sub_im'

name_list = ['single.png', 'burst.png', 'full.png']
for name in name_list:
    screen = cv2.imread(os.path.join(from_dir, name))
    sub_im = screen[1128: 1153, 1496: 1942, :]
    # cv2.imshow('sub_im', sub_im)
    # cv2.waitKey(1000)
    sub_im = get_shield_im(sub_im)
    # cv2.imshow('sub_im', sub_im)
    # cv2.waitKey(1000)
    cv2.imwrite(os.path.join(to_dir, name), sub_im)
