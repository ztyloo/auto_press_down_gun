import threading
import time
import cv2
import numpy as np
from PIL import ImageGrab
from pykeyboard import PyKeyboardEvent

from tab_detection.detect import Tab
from b_detection.fire_mode_detection import Bb
from auto_press_gun.press import Auto_down

single_shot_gun = ['98k', 'awm', 'm16', 'm24', 'mini14', 's12k', 's1987', 's686', 'sks', 'slr', 'win94']
full_shot_gun = ['dp28', 'm249']
single_burst_gun = ['m16', ]
full_mode_gun = ['akm', 'aug', 'groza', 'm416', 'm762', 'qbz', 'scar',  'ump9','vector']  # 'mk14', 'tommy', 'uzi', 'vss',

class Key_Listener(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)
        self.t = Tab()
        self.b = Bb()
        self.ad = Auto_down()
        self.t_set = False
        self.gun_name = 'none'
        self.scope_time = 1
        self.gun_name_ = 'none'
        self.scope_time_ = 1
        self.now_gun = self.gun_name
        self.now_scope = self.scope_time

    def tap(self, keycode, character, press):
        if keycode == 9 and press:  # tab
            self.ad.m_listener_stop()
            screen = self.get_screen()
            self.t.set_screen(screen)
            if self.t.test():
                self.gun_name = self.t.gun_name
                self.scope_time = self.t.scope_time
                self.gun_name_ = self.t.gun_name_
                self.scope_time_ = self.t.scope_time_
                self.now_gun = self.gun_name
                self.now_scope = self.scope_time
                threading.Timer(0.5, self.check_fire_mode).start()

        if keycode == 123 and press:  # F12
            self.ad.m_listener_stop()

        if keycode == 66 and not press:  # b
            threading.Timer(0.2, self.check_fire_mode).start()

        if keycode == 49 and press:  # 1
            self.now_gun = self.gun_name
            self.now_scope = self.scope_time
            print('now_gun', self.now_gun)
            threading.Timer(0.2, self.check_fire_mode).start()

        if keycode == 50 and press:  # 2
            self.now_gun = self.gun_name_
            self.now_scope = self.scope_time_
            print('now_gun', self.now_gun)
            threading.Timer(0.2, self.check_fire_mode).start()

    def check_fire_mode(self):
        if self.now_gun in full_mode_gun:
            screen = self.get_screen()
            self.b.set_screen(screen)
            self.b.test()
            if self.b.mode == 'full' and self.now_gun != 'none':
                self.ad.reset(self.now_gun, self.now_scope)
                self.ad.m_listener_run()
            else:
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