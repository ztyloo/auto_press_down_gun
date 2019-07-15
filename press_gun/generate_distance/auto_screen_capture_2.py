import os
import win32api
import win32con
import time
from pykeyboard import PyKeyboardEvent

from all_states import All_States
from press_gun.generate_distance.find_bullet_hole import find_bullet_hole, is_there_bullet_hole
from press_gun.generate_distance.find_aim_point import find_aim_point
from image_detect.detect import Detector
from auto_position_label.crop_position import crop_screen, screen_position as sc_pos
from screen_capture import win32_cap


def mouse_move(dx, dy):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(dx), int(dy))


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
        screen = win32_cap(self.all_states.weapon[0].name+'/0.png', (1500, 250, 1900, 1150))
        while is_there_bullet_hole(screen, None):
            mouse_move(0, -100)
            time.sleep(0.05)
            self.hole_counter += 1
            save_path = os.path.join(save_fold, str(self.hole_counter)+'.png')
            screen = win32_cap(save_path, (1400, 250, 2000, 1150))



if __name__ == '__main__':
    states = All_States()
    kl = Capture_Listener(states)
    kl.run()
