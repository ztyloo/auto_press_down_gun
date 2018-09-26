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

dir = 'ground'
to_a_dir = os.path.join(to_pos, dir)
if not os.path.exists(to_a_dir):
    os.mkdir(to_a_dir)
a_dir = os.path.join(pos_from, dir)
for name in os.listdir(a_dir):
    a_name = os.path.join(a_dir, name)
    im = cv2.imread(a_name)

    for i in range(13):
        sub_im = get_pos_im(yml, 'ground_'+str(i), im)
        if np.max(sub_im) == 255:
            cv2.imwrite(os.path.join(to_a_dir, name[:-4]+'_'+str(i)+'.png'), sub_im)

