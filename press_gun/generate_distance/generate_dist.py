import cv2
import os

from press_gun.generate_distance.find_bullet_hole import search_for_bullet_hole
from press_gun.generate_distance.find_aim_point import search_for_aim_point
from gun_modes import can_full_guns


gun_dist_dict = dict()
for gun_name in can_full_guns:
    one_gun_dist_list = list()
    for i in range(len(os.listdir(gun_name))):
        im_path = os.path.join(gun_name, str(i) + '.png')
        screen = cv2.imread(im_path)

        x0, y0 = search_for_aim_point(screen)

        aim_point = search_for_aim_point(screen)
        bullet_hole_centers_up = search_for_bullet_hole(screen, rect=(1500, 250, 1900, aim_point[1]-10))
        bullet_hole_centers_down = search_for_bullet_hole(screen, rect=(1500, aim_point[1]+10, 1900, 1050))

        i1, j1 = bullet_hole_centers_up[-1]
        i2, j2 = bullet_hole_centers_down[0]

        # screen = cv2.circle(screen, (x0, y0), 5, (0, 255, 255), thickness=20)
        # screen = cv2.circle(screen, (i1, j1), 5, (255, 0, 255), thickness=20)
        # screen = cv2.circle(screen, (i2, j2), 5, (255, 255, 0), thickness=20)
        # cv2.imshow('', screen)
        # cv2.waitKey()

        one_gun_dist_list.append(int((j2 - j1) / 12))

    gun_dist_dict[gun_name] = one_gun_dist_list

print(gun_dist_dict)