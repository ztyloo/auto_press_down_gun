import threading
import time
import cv2
import numpy as np
from pykeyboard import PyKeyboardEvent

from tab_detection.tab_detection import Tab_Detector
from b_detection.b_detection import B_Detector
from auto_press_gun.press import Auto_down
from lists import *
from all_state import State
from utils import get_screen


class Key_Listener(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)
        self.all_state = State()

        self.t = Tab_Detector(self.all_state)
        self.b = B_Detector(self.all_state)
        self.ad = Auto_down()

    def tap(self, keycode, character, press):

        if keycode == 9 and press:  # tab
            self.ad.m_listener_stop()
            screen = get_screen()
            threading.Timer(0.01, self.t.detect, args=[screen]).start()
            threading.Timer(0.5, self.check_fire_mode).start()

        if keycode == 123 and press:  # F12
            self.ad.m_listener_stop()

        if keycode == 71 and press:  # F12
            self.ad.m_listener_stop()

        if keycode == 66 and not press:  # b
            threading.Timer(0.1, self.check_fire_mode).start()

        if keycode == 49 and press:  # 1
            self.all_state.gun_state = 1
            self.all_state.update()
            print('gun0_name', self.all_state.gun0)
            threading.Timer(0.1, self.check_fire_mode).start()

        if keycode == 50 and press:  # 2
            self.all_state.gun_state = 2
            self.all_state.update()
            print('gun0_name', self.all_state.gun0)
            threading.Timer(0.1, self.check_fire_mode).start()

    def check_fire_mode(self):
        self.all_state.update()
        if self.all_state.gun0 in full_mode_gun:
            screen = get_screen()
            self.b.detect(screen)
            print(self.all_state.fire_mode1)
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