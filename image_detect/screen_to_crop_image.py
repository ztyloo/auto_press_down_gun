import cv2
import os
import numpy as np

from image_detect.crop_position import position


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


def white_shield_screen_to_crop(from_dir, crop_position):
    to_dir = from_dir[:-7]
    os.makedirs(to_dir, exist_ok=True)
    for name in os.listdir(from_dir):
        abs_screen_name = os.path.join(from_dir, name)
        screen = cv2.imread(abs_screen_name)
        x0, x1, y0, y1 = crop_position['x0'], crop_position['x1'], crop_position['y0'], crop_position['y1']
        crop_im = screen[y0: y1, x0: x1, :]
        shield_im = get_white_shield_im(crop_im)
        cv2.imwrite(os.path.join(to_dir, name), shield_im)


def diff_shield_screen_to_crop(from_dir, crop_position):
    to_dir = from_dir[:-7]
    os.makedirs(to_dir, exist_ok=True)
    for name in os.listdir(from_dir):
        if name[:1] == '_':
            x0, x1, y0, y1 = crop_position['x0'], crop_position['x1'], crop_position['y0'], crop_position['y1']
            abs_screen_name0 = os.path.join(from_dir, name[1:])
            abs_screen_name1 = os.path.join(from_dir, name)
            screen0 = cv2.imread(abs_screen_name0)
            screen1 = cv2.imread(abs_screen_name1)
            crop_im0 = screen0[y0: y1, x0: x1, :]
            crop_im1 = screen1[y0: y1, x0: x1, :]
            shield_im = get_diff_shield_im(crop_im0, crop_im1)
            cv2.imwrite(os.path.join(to_dir, name[1:]), shield_im)


def interval_shield_screen_to_crop(from_dir, crop_position, mid, radius):
    to_dir = from_dir[:-7]
    os.makedirs(to_dir, exist_ok=True)
    for name in os.listdir(from_dir):
        abs_screen_name = os.path.join(from_dir, name)
        screen = cv2.imread(abs_screen_name)
        x0, x1, y0, y1 = crop_position['x0'], crop_position['x1'], crop_position['y0'], crop_position['y1']
        crop_im = screen[y0: y1, x0: x1, :]
        shield_im = get_interval_shield_im(crop_im, mid, radius)
        cv2.imwrite(os.path.join(to_dir, name), shield_im)


if __name__ == '__main__':

    from_dir = os.path.join(os.path.dirname(__file__), 'in_tab_screen')
    crop_position = position['in_tab']
    white_shield_screen_to_crop(from_dir, crop_position)

    from_dir = os.path.join(os.path.dirname(__file__), 'weapon_screen')
    crop_position = position['weapon_1']
    white_shield_screen_to_crop(from_dir, crop_position)

    from_dir = os.path.join(os.path.dirname(__file__), 'scope_screen')
    crop_position = position['scope_1']
    diff_shield_screen_to_crop(from_dir, crop_position)

    from_dir = os.path.join(os.path.dirname(__file__), 'fire_mode_screen')
    crop_position = position['fire_mode']
    interval_shield_screen_to_crop(from_dir, crop_position, 205, 10)


