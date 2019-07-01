import os
import time
import cv2
import numpy as np
from PIL import ImageGrab


class Find_hole:
    def __init__(self, dx=100, dy=500):
        self.margin = 12
        self.y0 = 719
        self.x0 = 1719
        self.dx = dx
        self.dy = dy
        self.x1 = self.x0-dx
        self.x2 = self.x0+dx
        self.y1 = self.y0-dy
        self.y2 = self.y0-40
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
                # im = cv2.circle(screen, (i, j), 5, (0, 0, 255), thickness=20)
                # cv2.imshow('', im)
                # cv2.waitKey(1)

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
        g_ = 30
        l_ = 8
        for i in range(-l_, l_+1):
            r, g, b = area[y, x+i]
            if r>g_ or g>g_ or b>g_:
                return False
        for j in range(-l_, l_+1):
            r, g, b = area[y+j, x]
            if r>g_ or g>g_ or b>g_:
                return False
        return True


def find_upper(now_pos, screen):
    x0, y0 = now_pos
    for j in range(y0-5, y0-500, -1):
        for i in range(x0-100, x0+100):
            if is_point(screen, j, i):
                if is_end(screen, j, i):
                    return 0, 0
                return i, j
    return 0, 0


def is_point(area, y, x):
    g_ = 30
    l_ = 8
    for i in range(-l_, l_+1):
        r, g, b = area[y, x+i]
        if r>g_ or g>g_ or b>g_:
            return False
    for j in range(-l_, l_+1):
        r, g, b = area[y+j, x]
        if r>g_ or g>g_ or b>g_:
            return False
    return True


def is_end(area, y, x):
    g_ = 30
    counter = 0
    for i in range(-20, -10):
        r, g, b = area[y, x+i]
        if r<g_ and g<g_ and b<g_:
            counter += 1
            if counter > 10:
                return True
            continue
    for i in range(10, 20):
        r, g, b = area[y, x + i]
        if r < g_ and g < g_ and b < g_:
            counter += 1
            if counter > 10:
                return True
            continue
    for j in range(-20, -10):
        r, g, b = area[y+j, x]
        if r < g_ and g < g_ and b < g_:
            counter += 1
            if counter > 10:
                return True
            continue
    return False

if __name__ == '__main__':
    f = Find_hole()
    screen = cv2.imread('scar/test_point.png')
    i, j = f.find_upper(screen)
    screen = cv2.circle(screen, (i, j), 5, (0, 0, 255), thickness=20)

    i, j = f.find_lower(screen)
    screen = cv2.circle(screen, (i, j), 5, (0, 0, 255), thickness=20)
    cv2.imwrite('scar/' + '_' + str(1) + '.png', screen)