import threading
import time
import cv2
import numpy as np
from pykeyboard import PyKeyboardEvent
from PIL import ImageGrab
import itchat

from auto_press_gun.press import Auto_down
from lists import *
from all_state import State
from image_detect.detect import Detector


def get_screen():
    screen = ImageGrab.grab()
    screen = np.array(screen)
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    return screen


class Key_Listener(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)
        self.all_state = State()

        self.fire_mode_detect = Detector('fire_mode', 'fire_mode')
        self.in_tab_detect = Detector('in_tab', 'in_tab')

        self.weapon_1_detect = Detector('weapon_1', 'weapon')
        self.scope_1_detect = Detector('scope_1', 'scope')
        self.muzzle_1_detect = Detector('muzzle_1', 'muzzle')
        self.grip_1_detect = Detector('grip_1', 'grip')

        self.weapon_2_detect = Detector('weapon_2', 'weapon')
        self.scope_2_detect = Detector('scope_2', 'scope')
        self.muzzle_2_detect = Detector('muzzle_2', 'muzzle')
        self.grip_2_detect = Detector('grip_2', 'grip')

        self.ad = Auto_down()
        # itchat.auto_login(hotReload=True)
        print('Initial done!!!')

    def tab_func(self):
        self.ad.m_listener_stop()
        screen = get_screen()
        if 'in' == self.in_tab_detect(screen):
            self.all_state.weapon_1 = self.weapon_1_detect(screen)
            self.all_state.scope_1 = self.scope_1_detect(screen)
            self.all_state.muzzle_1 = self.muzzle_1_detect(screen)
            self.all_state.grip_1 = self.grip_1_detect(screen)

            self.all_state.weapon_2 = self.weapon_2_detect(screen)
            self.all_state.scope_2 = self.scope_2_detect(screen)
            self.all_state.muzzle_2 = self.muzzle_2_detect(screen)
            self.all_state.grip_2 = self.grip_2_detect(screen)

    def b_func(self):
        screen = get_screen()
        if self.all_state.now_weapon == 1:
            self.all_state.fire_mode_1 = self.fire_mode_detect(screen)
        elif self.all_state.now_weapon == 2:
            self.all_state.fire_mode_2 = self.fire_mode_detect(screen)
        else:
            raise Exception('now_weapon error')

    def ad_stop_func(self):
        self.ad.m_listener_stop()

    def set_auto_down(self):
        if self.all_state.now_weapon == 1:
            if self.all_state.weapon_1 in full_mode_gun and self.all_state.fire_mode_1 == 'full':
                self.ad.reset(self.all_state.weapon_1, self.all_state.scope_1)
                self.ad.m_listener_run()
            else:
                self.ad.m_listener_stop()
        elif self.all_state.now_weapon == 2:
            if self.all_state.weapon_2 in full_mode_gun and self.all_state.fire_mode_2 == 'full':
                self.ad.reset(self.all_state.weapon_2, self.all_state.scope_2)
                self.ad.m_listener_run()
            else:
                self.ad.m_listener_stop()
        else:
            raise Exception('now_weapon error')

    def tap(self, keycode, character, press):
        print(keycode, character, press)
        if keycode == 9 and press:  # tab
            threading.Timer(0.001, self.tab_func).start()

        if keycode == 123 and press:  # F12
            threading.Timer(0.001, self.ad_stop_func).start()

        if keycode == 71 and press:  # g
            threading.Timer(0.001, self.ad_stop_func).start()

        if keycode == 53 and press:  # 5
            threading.Timer(0.001, self.ad_stop_func).start()

        if keycode == 66 and not press:  # b
            threading.Timer(0.1, self.b_func).start()

        if keycode == 49 and press:  # 1
            self.all_state.gun_state = 1

        if keycode == 50 and press:  # 2
            self.all_state.gun_state = 2

        threading.Timer(0.001, self.set_auto_down).start()

    def escape(self, event):
        return False


k = Key_Listener()
k.run()