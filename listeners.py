import threading
import cv2
import numpy as np
from pykeyboard import PyKeyboardEvent
from PIL import ImageGrab
import itchat

from lists import *
from image_detect.detect import Detector
from auto_press_gun.press_listener import Press_Listener
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

        self.fire_mode_detect = Detector('fire_mode')
        self.in_tab_detect = Detector('in_tab')
        self.in_scope_detect = Detector('in_scope')

        self.name_detect = Detector('name')
        self.scope_detect = Detector('scope')
        # self.muzzle_detect = Detector('muzzle')
        # self.grip_detect = Detector('grip')

        self.press_listener = Press_Listener()
        # itchat.auto_login(hotReload=True)
        # itchat.send('Initial done!!!')
        print('Initial done!!!')

    def tap(self, keycode, character, press):
        if keycode == 9 and press:  # tab
            threading.Timer(0.001, self.tab_func).start()

        if keycode == 123 and press:  # F12
            threading.Timer(0.001, self.press_listener.stop()).start()

        if keycode == 71 and press:  # g
            threading.Timer(0.001, self.press_listener.stop()).start()

        if keycode == 53 and press:  # 5
            threading.Timer(0.001, self.press_listener.stop()).start()

        if keycode == 66 and press:  # b
            threading.Timer(0.5, self.b_func).start()

        if keycode == 49 and press:  # 1
            self.all_states.weapon_n = 0
            threading.Timer(0.001, self.set_auto_down).start()

        if keycode == 50 and press:  # 2
            self.all_states.weapon_n = 1
            threading.Timer(0.001, self.set_auto_down).start()

    def escape(self, event):
        return False

    def tab_func(self):
        self.all_states.in_tab = False
        self.press_listener.stop()
        screen = get_screen()
        if 'in' == self.in_tab_detect.diff_sum_classify(crop_screen(screen, sc_pos['in_tab'])):
            self.all_states.in_tab = True
            for n in [0, 1]:
                name_crop = crop_screen(screen, sc_pos['weapon'][n]['name'])
                scope_crop = crop_screen(screen, sc_pos['weapon'][n]['scope'])
                # muzzle_crop = crop_screen(screen, sc_pos['weapon'][n]['muzzle'])
                # grip_crop = crop_screen(screen, sc_pos['weapon'][n]['grip'])
                self.all_states.weapon[n].name = self.name_detect.diff_sum_classify(name_crop)
                self.all_states.weapon[n].scope = self.scope_detect.diff_sum_classify(scope_crop, sum_thr=10)
                # self.all_states.weapon[n].muzzle = self.muzzle_detect.diff_sum_classify(muzzle_crop)
                # self.all_states.weapon[n].grip = self.grip_detect.diff_sum_classify(grip_crop)

            print_state(self.all_states)
            self.set_auto_down()

    def b_func(self):
        self.press_listener.stop()

        screen = get_screen()
        fire_mode_crop = crop_screen(screen, sc_pos['fire_mode'])
        n = self.all_states.weapon_n
        self.all_states.weapon[n].fire_mode = self.fire_mode_detect.water_mark_classify(fire_mode_crop)

        print_state(self.all_states)
        self.set_auto_down()

    def set_auto_down(self):
        self.press_listener.stop()
        self.press_listener.press.set_states(self.all_states)

        n = self.all_states.weapon_n
        if self.all_states.weapon[n].fire_mode == 'full':
            self.press_listener.start()

def print_state(all_states):
    # n = all_states.weapon_n
    # print_str = str(all_states.weapon[n].name) + ' ' + str(all_states.weapon[n].scope) + ' ' + str(all_states.fire_mode)
    # print(print_str)
    # itchat.send('\n')
    # itchat.send(print_str)

    print(str(all_states.weapon_n))
    for n in [0, 1]:
        w = all_states.weapon[n]
        print(str(w.name) + ' ' + str(w.scope) + ' ' + str(w.fire_mode))

