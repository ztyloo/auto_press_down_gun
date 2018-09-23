import cv2
import os
import sys
import yaml

from generate_distance.find_point import Find


gun_name_list = ['98k', 'akm', 'aug', 'awm', 'dp28', 'groza', 'm16', 'm24', 'm249', 'm416', 'm762', 'mini14', 'mk14',
                 'mk47', 'qbu', 'qbz', 's12k', 's1987', 's686', 'scar', 'sks', 'slr', 'tommy', 'ump9', 'uzi', 'vector',
                 'vss', 'win94']


f = Find()
with open('gun_distance.yaml', 'w') as dumpfile:
    gun_dis_dict = dict()
    for gun_name in gun_name_list:
        if os.path.exists(gun_name):
            res_list = []
            for i in range(len(os.listdir(gun_name))):
                im_path = os.path.join(gun_name, str(i) + '.png')
                im = cv2.imread(im_path)
                # cv2.imshow('', im)
                i1, j1 = f.find_upper(im)
                i2, j2 = f.find_lower(im)
                im = cv2.circle(im, (i1, j1), 5, (0, 0, 255), thickness=20)
                im = cv2.circle(im, (i2, j2), 5, (0, 0, 255), thickness=20)
                cv2.imshow('', im)
                cv2.waitKey(1000)
                res_list.append((j2 - j1 + 4) / 12)

            gun_dis_dict[gun_name] = res_list


    dumpfile.write(yaml.dump(gun_dis_dict))