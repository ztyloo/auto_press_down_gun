import cv2
import os
import yaml
import numpy as np


# im2 = cv2.imread('tab_detection/pos_from/weapon_screen/98k.png')
# im2 = cv2.imread('b_detection/screens/burst.png')
im1 = cv2.imread('ctrl_cap/scar.png')
# im1 = cv2.imread('ctrl_cap/akm.png')
# im1 = cv2.imread('ctrl_cap/m416.png')
# im1 = cv2.imread('ctrl_cap/qbz.png')
im2 = cv2.imread('ctrl_cap/akm.png')


def im_norm(im: np.ndarray):
    avr = int(np.mean(im))
    im = im-avr
    return im

def get_shield(im: np.ndarray):
    im = im_norm(im)
    im_1 = im.max(axis=-1)
    shield = np.where(im_1 > 128, 255, 0).astype(np.uint8)
    return shield


def get_shield_im(im: np.ndarray):
    shield =get_shield(im)
    shield_im = np.concatenate((im, shield[:, :, np.newaxis]), axis=-1)
    return shield_im


im1 = im1[1176:1187, 1670:1768, :]
sheild1 = get_shield(im1)
sheild2 = get_shield(im2)


cv2.imshow('sheild1', sheild1)
# cv2.imshow('sheild1', sheild1)

# cv2.imshow('sheild', sheild1-sheild2)
# cv2.imshow('im', im1-im2)
cv2.waitKey(0)

