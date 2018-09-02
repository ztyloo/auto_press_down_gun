import cv2
import time
import numpy as np
from PIL import ImageGrab

from pymouse import PyMouseEvent
from pykeyboard import PyKeyboardEvent


class TapRecord(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)

    def tap(self, keycode, character, press):
        print(time.time()       , keycode, character, press)

t = TapRecord()
t.run()

