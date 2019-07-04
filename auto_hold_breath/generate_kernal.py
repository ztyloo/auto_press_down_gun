import cv2
import numpy as np

save_root = 'D:/github_project/auto_press_down_gun/auto_hold_breath/kernal_image/'

s4 = 'D:/github_project/auto_press_down_gun/auto_hold_breath/kernal_screen/4.png'
s6 = 'D:/github_project/auto_press_down_gun/auto_hold_breath/kernal_screen/6.png'
s8 = 'D:/github_project/auto_press_down_gun/auto_hold_breath/kernal_screen/8.png'
s15 = 'D:/github_project/auto_press_down_gun/auto_hold_breath/kernal_screen/15.png'
scope_list = [s4, s6, s8, s15]

c4 = [1718.5, 719.5]
c6 = [1718, 720]
c8 = [1715, 683]
c15 = [1723.5, 645.5]
center_list = [c4, c6, c8, c15]

radius = 100
for s, c in zip(scope_list, center_list):
    s_im = cv2.imread(s)
    cx, cy = c
    s_im_crop = s_im[int(np.floor(cy-radius)):int(np.ceil(cy+radius+1)), int(np.floor(cx-radius)):int(np.ceil(cx+radius+1))]

    im_grey = cv2.cvtColor(s_im_crop, cv2.COLOR_RGB2GRAY)
    im_kernal = np.where(im_grey <= 5, 255, 0).astype(np.uint8)

    cv2.imwrite(save_root+s.split('/')[-1], im_kernal)
