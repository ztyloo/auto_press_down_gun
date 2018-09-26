import cv2
import os
import yaml
import numpy as np


# im2 = cv2.imread('tab_detection/pos_from/weapon/98k.png')
# im2 = cv2.imread('b_detection/screens/burst.png')
im1 = cv2.imread('tab_detection/pos_/ground/153.png')
im2 = cv2.imread('tab_detection/pos_/ground/154.png')

def get_shield(im: np.ndarray):
    im_1 = im.max(axis=-1)
    shield = np.where(im_1 == 255, 255, 0).astype(np.uint8)
    return shield


def get_shield_im(im: np.ndarray):
    shield =get_shield(im)
    shield_im = np.concatenate((im, shield[:, :, np.newaxis]), axis=-1)
    return shield_im

sheild1 = get_shield(im1)
sheild2 = get_shield(im2)


cv2.imshow('sheild', sheild1-sheild2)
cv2.imshow('im', im1-im2)
cv2.waitKey(0)

