import os
import numpy as np
import cv2
import yaml
from pykeyboard import PyKeyboardEvent, PyKeyboard
from PIL import ImageGrab

from generate_distance.find_point import find_upper
import win32api
import win32con


def get_screen():
    screen = ImageGrab.grab()
    screen = np.array(screen)
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    return screen


def move(x, y):
    try:
        x = int(x)
        y = int(y)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y)
    except:
        print('Move Error')



class Key_Listener(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)
        self.gun_name_detector = Gun_Name_Detector()
        self.yml = yaml.load(open("../tab_detection/tab_position.yaml"))
        self.gun_name = None

    def tap(self, keycode, character, press):
        if keycode == 9 and not press:  # tab
            screen = get_screen()
            im = get_pos_im(self.yml, screen, 'name')
            self.gun_name = self.gun_name_detector.detect(im)
            if self.gun_name is not None and os.path.exists(self.gun_name):
                os.mkdir(self.gun_name)
            print(self.gun_name)

        if keycode == 123 and press:  # F12
            assert self.gun_name is not None
            res_list = detect_bullet_holes(self.gun_name)
            open_save_yaml(self.gun_name, res_list)


def detect_bullet_holes(save_dir):
    k = 0
    res_list = []

    screen = get_screen()
    i0, j0 = find_upper((1719, 719), screen)

    while True:
        screen = get_screen()

        i1, j1 = find_upper((i0, j0), screen)
        if i1 == 0 and j1 == 0:
            break
        res_list.append((j0 - j1) / 12)

        screen = cv2.circle(screen, (i1, j1), 5, (0, 0, 255), thickness=20)
        cv2.imwrite(save_dir+str(k)+'.png', screen)

        i0, j0 = i1, j1
        k += 1
        move(0, (j1-j0)//2)

    return res_list


def open_save_yaml(gun_name: str, distance_list: list):
    with open('gun_distance.yaml', 'r') as dumpfile:
        gun_dis_dict = yaml.load(dumpfile)

    if gun_dis_dict is None:
        gun_dis_dict = dict()

    with open('gun_distance.yaml', 'w') as dumpfile:
        gun_dis_dict[gun_name] = distance_list
        dumpfile.write(yaml.dump(gun_dis_dict))


if __name__ == '__main__':
    k = Key_Listener()
    k.run()

