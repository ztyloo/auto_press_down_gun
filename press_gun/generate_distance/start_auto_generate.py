import threading
import cv2
import numpy as np
import win32api
import win32con
from pykeyboard import PyKeyboardEvent
from PIL import ImageGrab

from main import All_States
from press_gun.generate_distance.find_hole import Find_hole
from image_detect.detect import Detector
from auto_position_label.crop_position import crop_screen, screen_position as sc_pos


def get_screen():
    screen = ImageGrab.grab()
    screen = np.array(screen)
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    return screen


class Key_Listener(PyKeyboardEvent):
    def __init__(self, all_states):
        PyKeyboardEvent.__init__(self)

        self.all_states = all_states

        self.in_tab_detect = Detector('in_tab')
        self.name_detect = Detector('name')
        self.scope_detect = Detector('scope')

        self.f_h = Find_hole()

    def tap(self, keycode, character, press):
        if keycode == 9 and press:  # tab
            self.tab_func()

        if keycode == 162 and press:  # ctrl
            if self.all_states.weapon[0].name != '':
                self.start_screen_cap()

    def escape(self, event):
        return False

    def tab_func(self):
        screen = get_screen()
        if 'in' == self.in_tab_detect.diff_sum_classify(crop_screen(screen, sc_pos['in_tab'])):
            for n in [0, 1]:
                name_crop = crop_screen(screen, sc_pos['weapon'][str(n)]['name'])
                scope_crop = crop_screen(screen, sc_pos['weapon'][str(n)]['scope'])
                self.all_states.weapon[n].name = self.name_detect.diff_sum_classify(name_crop)
                self.all_states.weapon[n].scope = self.scope_detect.diff_sum_classify(scope_crop, absent_return="1")

    def start_screen_cap(self):
        res_list = []
        screen = get_screen()
        i1, j1 = self.f_h.find_upper(screen)
        i2, j2 = self.f_h.find_lower(screen)

        res_list.append((j2 - j1 + 4) / 12)

        print(self.all_states.weapon[0]['name'], )


def mouse_down(y):
    try:
        x = 0
        y = int(y)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y)
    except:
        print('Move Error')

if __name__ == '__main__':
    states = All_States()
