import cv2
import os
import sys
from record_line.find_point import Find


f = Find()
res_list = []
for i in range(len(os.listdir('screens'))):
    im_path = os.path.join('screens',str(i)+'.png')
    im = cv2.imread(im_path)
    # cv2.imshow('', im)
    i1, j1 = f.find_upper(im)
    i2, j2 = f.find_lower(im)
    im = cv2.circle(im, (i1, j1), 5, (0, 0, 255), thickness=20)
    im = cv2.circle(im, (i2, j2), 5, (0, 0, 255), thickness=20)
    cv2.imshow('', im)
    cv2.waitKey(1000)
    res_list.append((j2-j1+4)/12)

print(res_list)