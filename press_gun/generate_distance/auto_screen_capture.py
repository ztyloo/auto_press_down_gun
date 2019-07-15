import os
import win32api
import win32con
import time
import cv2
from pykeyboard import PyKeyboardEvent

from all_states import All_States
from press_gun.generate_distance.find_bullet_hole import find_bullet_hole, find_up_first, find_down_first
from auto_hold_breath.aim_point import Aim_Point
from image_detect.detect import Detector
from auto_position_label.crop_position import crop_screen, screen_position as sc_pos
from screen_capture import win32_cap


def move_mouse(dx, dy):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(dx//2), int(dy//2))


def move_screen_center_to(x, y):
    dx = x - 1720
    dy = y - 720
    move_mouse(dx, dy)


class Capture_Listener(PyKeyboardEvent):
    def __init__(self, all_states):
        PyKeyboardEvent.__init__(self)

        self.all_states = all_states
        self.res_list = []
        self.hole_counter = 0
        self.save_root = 'D:/github_project/auto_press_down_gun/press_gun/generate_distance'

        self.in_tab_detect = Detector('in_tab')
        self.name_detect = Detector('weapon1name')
        self.scope_detect = Detector('weapon1scope')

        self.aim_point = Aim_Point()

    def tap(self, keycode, character, press):
        if keycode == 9 and press:  # tab
            self.tab_func()

        if keycode == 82 and press:  # r
            self.hole_counter = 0

        if keycode == 162 and press:  # ctrl
            if self.all_states.weapon[0].name != '':
                self.cap_screens()

    def tab_func(self):
        screen = win32_cap('D:/github_project/auto_press_down_gun/temp_image/auto_screen_capture.png')
        if 'in' == self.in_tab_detect.diff_sum_classify(crop_screen(screen, sc_pos['in_tab'])):
            n = 0
            name_crop = crop_screen(screen, sc_pos['weapon1name'])
            scope_crop = crop_screen(screen, sc_pos['weapon1scope'])
            self.all_states.weapon[n].name = self.name_detect.diff_sum_classify(name_crop)
            self.all_states.weapon[n].scope = self.scope_detect.diff_sum_classify(scope_crop, absent_return="1")

            self.hole_counter = 0

    def cap_screens(self):
        save_fold = os.path.join(self.save_root, self.all_states.weapon[0].name)
        os.makedirs(save_fold, exist_ok=True)

        r_x0, r_y0, r_x1, r_y1 = 1520, 250, 1920, 1150
        self.hole_counter = 0
        while True:
            screen = win32_cap(rect=(r_x0, r_y0, r_x1, r_y1))
            hole_centers = find_bullet_hole(screen)
            if len(hole_centers) < 2:
                break
            x1 = hole_centers[-2][0] + r_x0
            y1 = hole_centers[-2][1] + r_y0

            win32_cap(self.all_states.weapon[0].name + '/' + str(self.hole_counter) + '.png', (r_x0, r_y0, r_x1, r_y1))
            time.sleep(0.1)
            move_screen_center_to(x1, y1-(r_y1-r_y0)//2+30)
            time.sleep(0.1)

            self.hole_counter += 1


if __name__ == '__main__':
    states = All_States()
    kl = Capture_Listener(states)
    kl.run()


