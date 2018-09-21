import os
import time
import cv2
import numpy as np
from pykeyboard import PyKeyboardEvent, PyKeyboard
from auto_press_gun.my_timer import MyTimer
from auto_hold_breath.win32_screen_shot import window_capture

class Key_listern(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)
        self.i = 0
        self.t = MyTimer(0.04, )
        self.k = PyKeyboard()
        self.images = []

    def screen_shot(self):
        screen = ImageGrab.grab()
        screen = np.array(screen)
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
        self.images.append(screen)

    def tap(self, keycode, character, press):
        if keycode == 80 and press:
            self.k.press_key(160)
            self.i += 1


kl = Key_listern()
kl.run()