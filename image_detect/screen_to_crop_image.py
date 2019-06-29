import cv2
import os
import numpy as np

from image_detect.crop_position import position


def get_interval_shield(im, mid, radius):
    shield = im[0].copy()
    shield = shield.mean(axis=-1)
    shield = np.where(abs(shield - mid) <= radius, 255, 0).astype(np.uint8)
    return shield


def get_interval_shield_im(im: np.ndarray, mid, radius):
    shield = get_interval_shield(im, mid, radius)
    shield_im = np.concatenate((im, shield[:, :, np.newaxis]), axis=-1)
    return shield_im


def get_same_shield(im_list):
    add_diff_same = np.zeros_like(im_list[0])
    for im in im_list:
        add_diff_same += np.abs(im - im_list[0])

    shield = add_diff_same.max(axis=-1)
    shield = np.where(shield == 0, 255, 0).astype(np.uint8)
    return shield


def get_same_shield_im(im_list):
    shield = get_same_shield(im_list)
    shield_im = np.concatenate((im_list[0], shield[:, :, np.newaxis]), axis=-1)
    return shield_im


def screen_to_crop(from_dir, to_im, crop_position, mid=255, radius=0):
    if os.path.isdir(from_dir) and len(os.listdir(from_dir)) > 1:
        crop_im_list = list()
        for name in os.listdir(from_dir):
            abs_screen_name = os.path.join(from_dir, name)
            screen = cv2.imread(abs_screen_name)
            x0, x1, y0, y1 = crop_position['x0'], crop_position['x1'], crop_position['y0'], crop_position['y1']
            crop_im = screen[y0: y1, x0: x1, :]
            crop_im_list.append(crop_im)

        crop_shield = get_same_shield_im(crop_im_list)

    else:
        if os.path.isdir(from_dir):
            name = os.listdir(from_dir)[0]
            abs_screen_name = os.path.join(from_dir, name)
        else:
            abs_screen_name = from_dir
        screen = cv2.imread(abs_screen_name)
        x0, x1, y0, y1 = crop_position['x0'], crop_position['x1'], crop_position['y0'], crop_position['y1']
        crop_im = screen[y0: y1, x0: x1, :]
        crop_shield = get_interval_shield_im(crop_im, mid, radius)

    cv2.imwrite(to_im, crop_shield)


if __name__ == '__main__':
    from_dir = 'D:/github_project/auto_press_down_gun/image_detect/screen_captures/in_scope_ims'
    to_im = 'D:/github_project/auto_press_down_gun/image_detect/states_4c_im/in_scope/in.png'
    screen_to_crop(from_dir, to_im, position['in_scope'])

    # from_dir = os.path.join(os.path.dirname(__file__), 'in_tab_screen')
    # crop_position = position['in_tab']
    # white_shield_screen_to_crop(from_dir, crop_position)
    #
    # from_dir = os.path.join(os.path.dirname(__file__), 'weapon_screen')
    # crop_position = position['weapon_1']
    # white_shield_screen_to_crop(from_dir, crop_position)
    #
    # from_dir = os.path.join(os.path.dirname(__file__), 'scope_screen')
    # crop_position = position['scope_1']
    # diff_shield_screen_to_crop(from_dir, crop_position)
    #
    # from_dir = os.path.join(os.path.dirname(__file__), 'fire_mode_screen')
    # crop_position = position['fire_mode']
    # interval_shield_screen_to_crop(from_dir, crop_position, 205, 10)
    #


