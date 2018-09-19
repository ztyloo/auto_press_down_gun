import cv2
import os
import sys
from record_line.find_point import Find


f = Find()
res_list = []
for i in range(len(os.listdir('screens'))):
    im_path = os.path.join('screens',str(i)+'.jpg')
    im = cv2.imread(im_path)
    i1, j1 = f.find_upper(im)
    i2, j2 = f.find_lower(im)
    res_list.append(j2-j1)

print(res_list)