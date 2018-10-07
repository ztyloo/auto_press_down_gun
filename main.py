import threading
import time
import cv2
import numpy as np
from PIL import ImageGrab
from pykeyboard import PyKeyboardEvent

from tab_detection.tab_detection import Tab_Detector
from b_detection.fire_mode_detector import B_Detector
from auto_press_gun.press import Auto_down
from lists import *
from all_state import State
from utils import get_screen


class Key_Listener(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)
        self.state = State()

        self.t = Tab_Detector(self.state)
        self.b = B_Detector(self.state)
        self.ad = Auto_down()

    def tap(self, keycode, character, press):
        if keycode == 9 and press:  # tab
            self.ad.m_listener_stop()
            screen = get_screen()
            threading.Timer(0.01, self.t.detect, args=[screen]).start()
            threading.Timer(0.5, self.check_fire_mode).start()

        if keycode == 123 and press:  # F12
            self.ad.m_listener_stop()

        if keycode == 66 and not press:  # b
            threading.Timer(0.1, self.check_fire_mode).start()

        if keycode == 49 and press:  # 1
            self.state.use_gun1()
            print('gun_state', self.state.gun0)
            threading.Timer(0.1, self.check_fire_mode).start()

        if keycode == 50 and press:  # 2
            self.state.use_gun2()
            print('gun_state', self.state.gun0)
            threading.Timer(0.1, self.check_fire_mode).start()

    def check_fire_mode(self):
        if self.state.gun0 in full_mode_gun:
            screen = get_screen()
            self.b.set_screen(screen)
            self.b.test()
            if self.b.mode == 'full' and self.now_gun != 'none':
                self.ad.reset(self.now_gun, self.now_scope)
                self.ad.m_listener_run()
            else:
                self.ad.m_listener_stop()


    def escape(self, event):
        return False

k = Key_Listener()
k.run()