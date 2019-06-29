import cv2
import os
import numpy as np

from image_detect.crop_position import position


def get_interval_shield(im, mid, radius):
    shield = im.copy()
    shield = shield.mean(axis=-1)
    shield = np.where(abs(shield - mid) <= radius, 255, 0).astype(np.uint8)
    return shield


def get_interval_shield_im(im: np.ndarray, mid, radius):
    shield = get_interval_shield(im, mid, radius)
    shield_im = np.concatenate((im, shield[:, :, np.newaxis]), axis=-1)
    return shield_im


def get_similar_shield(im_list, radius):
    add_im_diff = np.zeros_like(im_list[0])
    for im in im_list:
        add_im_diff += np.abs(im - im_list[0])

    average_im_diff = add_im_diff/len(im_list)

    shield = average_im_diff.max(axis=-1)
    shield = np.where(shield <= radius, 255, 0).astype(np.uint8)
    return shield


def get_similar_shield_im(im_list, radius):
    shield = get_similar_shield(im_list, radius)
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

        crop_shield = get_similar_shield_im(crop_im_list, radius=0)

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
    all_from_dir = 'D:/github_project/auto_press_down_gun/image_detect/screen_captures/'
    all_to_dir = 'D:/github_project/auto_press_down_gun/image_detect/states_4c_im/'

    for clas in os.listdir(all_from_dir):
        temp_dir = os.path.join(all_from_dir, clas)
        for state in os.listdir(temp_dir):
            from_dir = os.path.join(all_from_dir, clas, state)
            to_im = os.path.join(all_to_dir, clas, state+'.png')
            screen_to_crop(from_dir, to_im, position['in_scope'])

    # from_dir = 'D:/github_project/auto_press_down_gun/image_detect/screen_captures/in_scope'
    # to_im = 'D:/github_project/auto_press_down_gun/image_detect/states_4c_im/in_scope/in.png'
    # screen_to_crop(from_dir, to_im, position['in_scope'])

    # from_dir = 'D:/github_project/auto_press_down_gun/image_detect/screen_captures/full'
    # to_im = 'D:/github_project/auto_press_down_gun/image_detect/states_4c_im/fire_mode/full.png'
    # screen_to_crop(from_dir, to_im, position['fire_mode'], mid=215, radius=15)
    #
    # from_dir = 'D:/github_project/auto_press_down_gun/image_detect/screen_captures/burst'
    # to_im = 'D:/github_project/auto_press_down_gun/image_detect/states_4c_im/fire_mode/burst.png'
    # screen_to_crop(from_dir, to_im, position['fire_mode'], mid=215, radius=15)
    #
    # from_dir = 'D:/github_project/auto_press_down_gun/image_detect/screen_captures/single'
    # to_im = 'D:/github_project/auto_press_down_gun/image_detect/states_4c_im/fire_mode/single.png'
    # screen_to_crop(from_dir, to_im, position['fire_mode'], mid=215, radius=15)

    # for png_path in os.listdir('D:/github_project/auto_press_down_gun/image_detect/screen_captures/weapon'):
    #     from_dir = 'D:/github_project/auto_press_down_gun/image_detect/screen_captures/weapon/' + png_path
    #     to_im = 'D:/github_project/auto_press_down_gun/image_detect/states_4c_im/weapon/' + png_path
    #     screen_to_crop(from_dir, to_im, position['weapon_1'])
    #
    # from_dir = 'D:/github_project/auto_press_down_gun/image_detect/screen_captures/in_scope'
    # to_im = 'D:/github_project/auto_press_down_gun/image_detect/states_4c_im/in_scope/in.png'
    # screen_to_crop(from_dir, to_im, position['in_scope'])
