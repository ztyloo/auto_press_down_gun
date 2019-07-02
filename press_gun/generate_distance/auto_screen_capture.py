import cv2
import os
import numpy as np
import win32api
import win32con
from pykeyboard import PyKeyboardEvent
from PIL import ImageGrab

from main import All_States
from press_gun.generate_distance.find_bullet_hole import search_for_bullet_hole
from image_detect.detect import Detector
from auto_position_label.crop_position import crop_screen, screen_position as sc_pos


def get_screen():
    screen = ImageGrab.grab()
    screen = np.array(screen)
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    return screen


class Capture_Listener(PyKeyboardEvent):
    def __init__(self, all_states):
        PyKeyboardEvent.__init__(self)

        self.all_states = all_states
        self.res_list = []
        self.hole_counter = 0
        self.save_root = 'D:/github_project/auto_press_down_gun/press_gun/generate_distance'

        self.in_tab_detect = Detector('in_tab')
        self.name_detect = Detector('name')
        self.scope_detect = Detector('scope')

    def tap(self, keycode, character, press):
        if keycode == 9 and press:  # tab
            self.tab_func()

        if keycode == 162 and press:  # ctrl
            if self.all_states.weapon[0].name != '':
                self.cap_a_screen()

    def tab_func(self):
        screen = get_screen()
        if 'in' == self.in_tab_detect.diff_sum_classify(crop_screen(screen, sc_pos['in_tab'])):
            n = 0
            name_crop = crop_screen(screen, sc_pos['weapon'][str(n)]['name'])
            scope_crop = crop_screen(screen, sc_pos['weapon'][str(n)]['scope'])
            self.all_states.weapon[n].name = self.name_detect.diff_sum_classify(name_crop)
            self.all_states.weapon[n].scope = self.scope_detect.diff_sum_classify(scope_crop, absent_return="1")

            self.hole_counter = 0

    def cap_a_screen(self):
        screen = get_screen()
        bullet_hole_centers = search_for_bullet_hole(screen, rect=(1500, 250, 1900, 719))
        if len(bullet_hole_centers) == 0:
            return
        else:
            next_center_x = bullet_hole_centers[-1][0]
            print()
            next_center_y = bullet_hole_centers[-1][1] - 0
            mv_x = next_center_x-1719
            mv_y = next_center_y-719
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(mv_x//3), int(mv_y//3))

            save_path = os.path.join(self.save_root, self.all_states.weapon[0].name, str(self.hole_counter)+'.png')
            cv2.imwrite(save_path, screen)


if __name__ == '__main__':
    states = All_States()
    kl = Capture_Listener(states)
    kl.run()
