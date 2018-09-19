import os
import time
import cv2
import numpy as np
from PIL import ImageGrab
from pykeyboard import PyKeyboardEvent, PyKeyboard


class Key_listern(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)
        self.i = 0

    def tap(self, keycode, character, press):
        if keycode == 80 and press:
            screen = ImageGrab.grab()
            screen = np.array(screen)
            screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
            print('screens/' + str(self.i) + '.png')
            cv2.imwrite('screens/' + str(self.i) + '.png', screen)
            self.i += 1


kl = Key_listern()
kl.run()