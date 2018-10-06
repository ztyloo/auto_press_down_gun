import cv2
import os
import yaml
import numpy as np


def get_shield(im: np.ndarray):
    im_1 = im.max(axis=-1)
    shield = np.where(im_1 == 255, 255, 0).astype(np.uint8)
    return shield


def get_shield_im(im: np.ndarray):
    shield =get_shield(im)
    shield_im = np.concatenate((im, shield[:, :, np.newaxis]), axis=-1)
    return shield_im


yml = yaml.load(open("tab_position.yaml"))
pos_from = 'pos_'
to_pos = 'pos'

# name_filter = ['weapon', 'user']
# for dir in os.listdir(pos_from):
#     if dir in name_filter:
#         to_a_dir = os.path.join(to_pos, dir)
#         if not os.path.exists(to_a_dir):
#             os.mkdir(to_a_dir)
#         a_dir = os.path.join(pos_from, dir)
#         for name in os.listdir(a_dir):
#             a_name = os.path.join(a_dir, name)
#             sub_im = cv2.imread(a_name)
#             sub_im = get_shield_im(sub_im)
#             cv2.imwrite(os.path.join(to_a_dir, name), sub_im)


a_name = 'pos_/user/time.png'
im = cv2.imread(a_name)
sub_im = get_shield_im(im)
cv2.imwrite(os.path.join('pos/user/', 'time.png'), sub_im)

