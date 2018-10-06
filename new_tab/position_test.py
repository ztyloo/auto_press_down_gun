import cv2
import numpy as np
import yaml


def get_pos(pos: str, im: np.ndarray):
    yml = yaml.load(open("tab_position.yaml"))
    x0 = yml[pos]['x0']
    x1 = yml[pos]['x1']
    y0 = yml[pos]['y0']
    y1 = yml[pos]['y1']
    return im[y0: y1, x0: x1, :]


im = cv2.imread('body_screens/32.png')
# im = cv2.imread()
# im = cv2.imread()



yml = yaml.load(open("tab_position.yaml"))
for k, v in yml.items():
    print(k)
    kim = get_pos(k, im)
    cv2.imshow(k, kim)
    cv2.waitKey(1000)



