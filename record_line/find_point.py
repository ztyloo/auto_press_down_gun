import os
import time
import cv2
import numpy as np
from PIL import ImageGrab


class Find:
    def __init__(self, dx=100, dy=500):
        self.margin = 12
        self.y0 = 719
        self.x0 = 1719
        self.dx = dx
        self.dy = dy
        self.x1 = self.x0-dx
        self.x2 = self.x0+dx
        self.y1 = self.y0-dy
        self.y2 = self.y0
        self.y3 = self.y0+dy

    def find_upper(self, img=None):
        if img is None:
            screen = ImageGrab.grab()
            screen = np.array(screen)
            screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
        else:
            screen = img
        for j in range(self.y2, self.y1, -1):
            for i in range(self.x1, self.x2):
                # print('checking:', i, j)
                if self.is_point(screen, j, i):
                    return i, j
        return 0, 0

    def find_lower(self, img=None):
        if img is None:
            screen = ImageGrab.grab()
            screen = np.array(screen)
            screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
        else:
            screen = img
        for j in range(self.y2, self.y3):
            for i in range(self.x1, self.x2):
                # print('checking:', i, j)
                if self.is_point(screen, j, i):
                    return i, j
        return 0, 0

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


if __name__ == '__main__':
    f = Find()
    screen = cv2.imread('screens/test_point.png')
    i, j = f.find_upper(screen)
    screen = cv2.circle(screen, (i, j), 5, (0, 0, 255), thickness=20)

    i, j = f.find_lower(screen)
    screen = cv2.circle(screen, (i, j), 5, (0, 0, 255), thickness=20)
    cv2.imwrite('screens/' + '_' + str(1) + '.png', screen)