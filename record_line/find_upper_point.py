import os
import time
import cv2
import numpy as np
from PIL import ImageGrab
from PIL import ImageGrab


class Find:
    def __init__(self, x1=-100, x2=100, y1=0, y2=500):
        x0 = 719
        y0 = 1719
        self.x1 = x1 - x0
        self.x2 = x2 - x0
        self.y1 = y1 - y0
        self.y2 = y2 - y0
        self.margin = 12

    def find_upper(self, img=None):
        if img is None:
            screen = ImageGrab.grab()
            screen = np.array(screen)
            screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
        else:
            screen = img
        search_area = screen[self.y1 - self.margin:self.y2 + self.margin, self.x1 - self.margin:self.x2 + self.margin, :]
        for j in range(self.y2 - self.y1, -1):
            for i in range(self.x2 - self.x1):
                i = i + self.margin
                j = j + self.margin
                print('checking:', i, j)
                if self.is_point(search_area, j, i):
                    return i ,j

    def is_point(self,area, y, x):
        for i in range(-10, 11):
            r, g, b = area[y, x+i]
            if r>30 or g>30 or b>30:
                return False
        for j in range(-10, 11):
            r, g, b = area[y+j, x]
            if r>30 or g>30 or b>30:
                return False
        return True


f = Find()
im = cv2.imread('test_point.png')
x, y = f.find_upper(im)
print(x, y)