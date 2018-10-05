import cv2
import yaml
from pykeyboard import PyKeyboardEvent, PyKeyboard

from utils import get_screen, move
from generate_distance.find_point import find_upper
from tab_detection.gun_name import Gun_Name_Detector
from tab_detection.utils import get_pos_im


class Key_Listener(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)
        self.gun_name_detector = Gun_Name_Detector()
        self.yml = yaml.load(open("tab_detection/tab_position.yaml"))
        self.gun_name = 'none'

    def tap(self, keycode, character, press):
        if keycode == 9 and not press:  # F11
            screen = get_screen()
            im = get_pos_im(self.yml, screen, 'weapon')
            self.gun_name = self.gun_name_detector.detect(im)

    def f12(self, keycode, character, press):
        if keycode == 123 and press:  # F12
            res_list = detect_bullet_holes()
            open_save_yaml(self.gun_name, res_list)


def detect_bullet_holes():
    k = 0
    res_list = []
    i0, j0 = 1719, 719

    while True:
        screen = get_screen()

        i1, j1 = find_upper(screen, (i0, j0))
        if i1 == 0 and j1 == 0:
            break
        res_list.append((j0 - j1) / 12)

        screen = cv2.circle(screen, (i1, j1), 5, (0, 0, 255), thickness=20)
        cv2.imwrite(str(k)+'.png', screen)

        i0, j0 = i1, j1
        k += 1
        move(0, j1-j0)

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
    k = PyKeyboard()
    k.run()

