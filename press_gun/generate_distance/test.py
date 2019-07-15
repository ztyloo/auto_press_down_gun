import cv2
import os
import numpy as np
from press_gun.generate_distance.find_bullet_hole import find_bullet_hole


save_fold = 'm762'


counter = 0
while os.path.exists(os.path.join(save_fold, str(counter) + '.png')):
    counter += 1

last_im = cv2.imread(os.path.join(save_fold, str(0)+'.png'))
for i in range(1, counter):
    last_im = cv2.imread(os.path.join(save_fold, str(i)+'.png'))

# last_im_path = os.path.join(save_fold, str(0)+'.png')
# last_im = cv2.imread(last_im_path)
# i = 1
# while True:
#     im_path = os.path.join(save_fold, str(i)+'.png')
#     if not os.path.exists(im_path):
#         break
#     im = cv2.imread(im_path)
#     im = im[:(im.shape[1]-200), :, :]
#     last_im = np.concatenate((im,last_im),axis=0)
#     i += 1
#     cv2.imshow('last_im', last_im)
#     cv2.waitKey()

