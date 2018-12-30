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


    def tap(self, keycode, character, press):
        print(keycode, character, press)
        if keycode == 9 and press:  # tab
            self.ad.m_listener_stop()
            threading.Timer(0.001, self.get_screen).start()
            threading.Timer(0.1, self.t.detect, args=[self.screen]).start()

        if keycode == 123 and press:  # F12
            self.ad.m_listener_stop()

        if keycode == 71 and press:  # g
            self.ad.m_listener_stop()

        if keycode == 66 and not press:  # b
            threading.Timer(0.1, self.check_fire_mode).start()

        if keycode == 49 and press:  # 1
            self.all_state.gun_state = 1
            self.all_state.update()
            print('gun0_name', self.all_state.gun0)

        if keycode == 50 and press:  # 2
            self.all_state.gun_state = 2
            self.all_state.update()
            print('gun0_name', self.all_state.gun0)

    def check_fire_mode(self):
        self.all_state.update()
        if self.all_state.gun0 in full_mode_gun:
            screen = get_screen()
            self.b.detect(screen)
            print(self.all_state.fire_mode1)
            itchat.send(str(self.all_state.gun0)+str(self.all_state.scope0)+str(self.all_state.fire_mode1))
            if self.all_state.fire_mode1 == 'full' and self.all_state.gun0 is not None:
                self.ad.reset(self.all_state.gun0, self.all_state.scope0)
                print(self.all_state.gun0, self.all_state.scope0)
                self.ad.m_listener_run()
            else:
                self.ad.m_listener_stop()

    def escape(self, event):
        return False


k = Key_Listener()
k.run()