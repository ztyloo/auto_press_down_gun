import cv2
import os
import numpy as np


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
    if len(os.listdir(from_dir)) > 1:
        crop_im_list = list()
        for name in os.listdir(from_dir):
            abs_screen_name = os.path.join(from_dir, name)
            screen = cv2.imread(abs_screen_name)
            x0, y0, x1, y1 = crop_position
            crop_im = screen[y0: y1, x0: x1, :]
            crop_im_list.append(crop_im)

        crop_shield = get_similar_shield_im(crop_im_list, radius=0)

    else:
        name = os.listdir(from_dir)[0]
        abs_screen_name = os.path.join(from_dir, name)
        screen = cv2.imread(abs_screen_name)
        x0, y0, x1, y1 = crop_position
        crop_im = screen[y0: y1, x0: x1, :]
        # cv2.imshow('', crop_im)
        # cv2.waitKey()
        crop_shield = get_interval_shield_im(crop_im, mid, radius)

    cv2.imwrite(to_im, crop_shield)


if __name__ == '__main__':
    from auto_position_label.crop_position import screen_position

    all_from_dir = 'D:/github_project/auto_press_down_gun/auto_position_label/screen_captures/'
    all_to_dir = 'D:/github_project/auto_press_down_gun/image_detect/states_4c_im/'

    for state in os.listdir(all_from_dir):
        from_dir = os.path.join(all_from_dir, state)
        pos, to_im = state.split('-')[0], state.split('-')[1]+'.png'
        to_fold = os.path.join(all_to_dir, pos)
        os.makedirs(to_fold, exist_ok=True)
        to_im_path = os.path.join(all_to_dir, pos, to_im)
        if 'fire_mode' in state:
            screen_to_crop(from_dir, to_im_path, screen_position[pos], mid=215, radius=15)
        else:
            screen_to_crop(from_dir, to_im_path, screen_position[pos])


