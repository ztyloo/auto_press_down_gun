import cv2
import os
import yaml
import numpy as np


def get_pos_im(yml: yaml, pos: str, im: np.ndarray):
    x0 = yml[pos]['x0']
    x1 = yml[pos]['x1']
    y0 = yml[pos]['y0']
    y1 = yml[pos]['y1']
    return im[y0: y1, x0: x1, :]


yml = yaml.load(open("tab_position.yaml"))
pos_from = 'pos_from'
to_pos = 'pos_'


# for dir in os.listdir(pos_from):
#     to_a_dir = os.path.join(to_pos, dir)
#     if not os.path.exists(to_a_dir):
#         os.mkdir(to_a_dir)
#     a_dir = os.path.join(pos_from, dir)
#     for name in os.listdir(a_dir):
#         a_name = os.path.join(a_dir, name)
#         im = cv2.imread(a_name)
#         sub_im = get_pos_im(yml, dir, im)
#         cv2.imwrite(os.path.join(to_a_dir, name), sub_im)


a_name = 'pos_from/user/time.png'
im = cv2.imread(a_name)
sub_im = get_pos_im(yml, 'user', im)
cv2.imwrite(os.path.join('pos_/', 'time.png'), sub_im)

