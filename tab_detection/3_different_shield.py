import cv2
import os
import yaml
import numpy as np


def get_shield(im0: np.ndarray, im1: np.ndarray):
    shield_ = (np.abs(im0 - im1)).max(axis=-1)
    shield = np.where(shield_ == 0, 255, 0).astype(np.uint8)
    return shield


def get_shield_im(im0: np.ndarray, im1: np.ndarray):
    shield =get_shield(im0, im1)
    shield_im = np.concatenate((im0, shield[:, :, np.newaxis]), axis=-1)
    return shield_im


yml = yaml.load(open("tab_position.yaml"))
pos_from = 'pos_'
to_pos = 'pos'

name_filter = ['scope']
for dir in os.listdir(pos_from):
    if dir in name_filter:
        to_a_dir = os.path.join(to_pos, dir)
        if not os.path.exists(to_a_dir):
            os.mkdir(to_a_dir)
        a_dir = os.path.join(pos_from, dir)
        for name in os.listdir(a_dir):
            if name[0] != '_':
                a_name = os.path.join(a_dir, name)
                a_name1 = os.path.join(a_dir, '_' + name)
                sub_im0 = cv2.imread(a_name)
                sub_im1 = cv2.imread(a_name1)
                sub_im = get_shield_im(sub_im0, sub_im1)
                cv2.imwrite(os.path.join(to_a_dir, name), sub_im)
