import cv2
import os

from press_gun.generate_distance.find_bullet_hole import find_bullet_hole
from press_gun.generate_distance.find_aim_point import find_aim_point
from all_states import can_full_guns


gun_dist_dict = dict()
for gun_name in can_full_guns:
    one_gun_dist_list = list()
    for i in range(len(os.listdir(gun_name))):
        im_path = os.path.join(gun_name, str(i) + '.png')
        screen = cv2.imread(im_path)

        x0, y0 = find_aim_point(screen)
        six_scope_radius = 480
        cv2.circle(screen, (x0, y0), 480+300, (255, 255, 255), 600)
        cv2.line(screen, (x0-(200+300), 0), (x0-(200+300), 1440), (255, 255, 255), 600)
        cv2.line(screen, (x0+(200+300), 0), (x0+(200+300), 1440), (255, 255, 255), 600)
        # cv2.imshow('screen', screen)
        # cv2.waitKey()

        bullet_hole_centers_up = find_bullet_hole(screen, rect=(1140, 140, 2350, y0))
        bullet_hole_centers_down = find_bullet_hole(screen, rect=(1140, y0, 2350, 1350))

        i1, j1 = bullet_hole_centers_up[-1]
        i2, j2 = bullet_hole_centers_down[0]

        screen = cv2.circle(screen, (x0, y0), 5, (0, 255, 255), thickness=20)
        screen = cv2.circle(screen, (i1, j1), 5, (255, 0, 255), thickness=20)
        screen = cv2.circle(screen, (i2, j2), 5, (255, 255, 0), thickness=20)
        cv2.imshow(gun_name, screen)
        cv2.waitKey(500)

        one_gun_dist_list.append(int((j2 - j1) / 12))

    print("'"+gun_name+"': " + str(one_gun_dist_list) + ',')
    gun_dist_dict[gun_name] = one_gun_dist_list

print(gun_dist_dict)