import cv2
import numpy as np

screen = cv2.imread('44.png')
ryanshuai_grab = screen[46:81, 1620:1818, :]
cv2.imwrite('origin.png', ryanshuai_grab)

shield = np.zeros_like(ryanshuai_grab)
for i, i_ in enumerate(ryanshuai_grab):
    for j, j_ in enumerate(i_):
        if j_[0] < 255 and j_[1] < 255 and j_[2] < 255:
            shield[i, j] = [0, 0, 0]
        else:
            shield[i, j] = [255, 255, 255]

cv2.imwrite('shield.png', shield)

