import threading
import time
import cv2
import numpy as np
from PIL import ImageGrab
from pykeyboard import PyKeyboardEvent

from tab_detection.detect import Tab
from b_detection.fire_mode_detection import Bb
from auto_press_gun.press import Auto_down


class Key_Listener(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)
        self.t = Tab()
        self.b = Bb()
        self.ad = Auto_down()
        self.t_set = False
        self.gun_name = 'none'
        self.scope_time = 1

    def tap(self, keycode, character, press):
        if keycode == 9 and press:  # tab
            self.ad.m_listener_stop()
            screen = self.get_screen()
            self.t.set_screen(screen)
            if self.t.test():
                self.gun_name = self.t.gun_name
                self.scope_time = self.t.scope_time
                threading.Timer(0.5, self.check_fire_mode).start()

        if keycode == 66 and not press:
            self.check_fire_mode()

    def check_fire_mode(self):
        screen = self.get_screen()
        self.b.set_screen(screen)
        self.b.test()
        if self.b.mode == 'full' and self.gun_name != 'none':
            self.ad.reset(self.gun_name, self.scope_time)
            self.ad.m_listener_run()
        else:
            print('stop press')
            self.ad.m_listener_stop()

    def get_screen(self):
        screen = ImageGrab.grab()
        screen = np.array(screen)
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)

        # screen = cv2.imread('')
        return screen

    def escape(self, event):
        return False

k = Key_Listener()
k.run()