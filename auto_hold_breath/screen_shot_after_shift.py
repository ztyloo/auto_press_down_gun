import os
import time
import cv2
import numpy as np
from pykeyboard import PyKeyboardEvent, PyKeyboard
from auto_press_gun.my_timer import MyTimer
from auto_hold_breath.win32_screen_shot import Screen

class Key_listern(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)
        self.i = 0
        self.t = MyTimer(0.04, self.screen_shot)
        self.k = PyKeyboard()
        self.sc = Screen()

    def screen_shot(self):
        self.sc.shot()

    def tap(self, keycode, character, press):
        print(keycode, press)
        if keycode == 160 and not press:
            self.t.start()
            self.t0 = time.time()

        if keycode == 48 and press:
            self.t.cancel()
            self.t1 = time.time()
            print(self.t1-self.t0)
            self.sc.save('screens/')


kl = Key_listern()
kl.run()