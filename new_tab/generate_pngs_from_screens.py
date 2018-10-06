import cv2
import os
import yaml
import numpy as np

from new_tab.tab_utils import get_pos_im
from lists import gun_name_list, scope_name_list


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


def find_position(name: str):
    if name in gun_name_list:
        return 'weapon'
    if name in scope_name_list:
        return 'scope'


if __name__ == '__main__':
    pos_white_list = ['weapon']
    pos_diff_list = ['scope']
    from_dir = 'screens'
    to_dir = 'pngs'

    yml = yaml.load(open("tab_position.yaml"))
    for im_name in os.listdir(from_dir):
        item_name = im_name[0: -4]
        pos = find_position(item_name)

        if pos in pos_white_list:
            from_im_path = os.path.join(from_dir, im_name)
            to_im_path = os.path.join(to_dir, im_name)

            screen = cv2.imread(from_im_path)
            sub_im = get_pos_im(yml, screen, pos)
            shield_im = get_white_shield_im(sub_im)
            cv2.imwrite(to_im_path, shield_im)

        if pos in pos_diff_list:
            to_im_path = os.path.join(to_dir, im_name)

            from_im_path = os.path.join(from_dir, im_name)
            _from_im_path = os.path.join(from_dir, '_'+im_name)

            screen = cv2.imread(from_im_path)
            screen_ = cv2.imread(_from_im_path)

            sub_im = get_pos_im(yml, screen, pos)
            sub_im_ = get_pos_im(yml, screen_, pos)

            shield_im = get_diff_shield_im(sub_im, sub_im_)
            cv2.imwrite(to_im_path, shield_im)