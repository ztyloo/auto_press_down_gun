import cv2
import os
import yaml
import numpy as np


def get_shield(im: np.ndarray):
    shield = im.copy()
    shield = shield.mean(axis=-1)
    shield = np.where(abs(shield-205) < 10, 255, 0).astype(np.uint8)

    # im = np.where(im > 50, 255, 0).astype(np.uint8)
    # im_mean = np.mean(im)
    # im = im - im_mean
    # im = np.where(im > 10, 255, 0).astype(np.uint8)

    return shield


def get_shield_im(im: np.ndarray):
    shield =get_shield(im)
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

