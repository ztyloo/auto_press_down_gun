import cv2
import os
import time
from pytesseract import image_to_string

dir = 'pos_/ground'

for im_name in os.listdir(dir):
    im = cv2.imread(os.path.join(dir, im_name))
    im = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
    cv2.imshow('', im)
    text = image_to_string(im)
    print(text)
    time.sleep(2)
