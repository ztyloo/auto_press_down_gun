import time
import cv2
import numpy as np
from PIL import ImageGrab
from pykeyboard import PyKeyboardEvent
from pymouse import PyMouseEvent


class TapRecord(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)
        self.i = 0

    def tap(self, keycode, character, press):
        if keycode == 9:
            screen = ImageGrab.grab()
            screen = np.array(screen)
            screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
            cv2.imwrite('tab_cap/' + str(self.i) + '_' + str(press) + '.png', screen)
            self.i += 1

            print(keycode)
            print(character)
            print(press)

    def escape(self, event):
        return False

t = TapRecord()
t.run()