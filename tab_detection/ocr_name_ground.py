import cv2
import os
import time
import numpy as np
from pytesseract import image_to_string

dir = 'pos_/ground'

def get_shield(im: np.ndarray):
    im_1 = im.max(axis=-1)
    shield = np.where(im_1 >190, 255, 0).astype(np.uint8)
    return shield

for im_name in os.listdir(dir):
    im = cv2.imread(os.path.join(dir, im_name))
    im = get_shield(im)
    text = image_to_string(im)
    print(text)
    cv2.imshow('', im)
    cv2.waitKey(1000)
