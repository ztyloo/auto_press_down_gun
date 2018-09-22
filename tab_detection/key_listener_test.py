import cv2
import time
import numpy as np
from PIL import ImageGrab

from pymouse import PyMouseEvent
from pykeyboard import PyKeyboardEvent


class Key_Listener(PyKeyboardEvent):
    def __init__(self, func):
        PyKeyboardEvent.__init__(self)
        self.func = func

    def tap(self, keycode, character, press):
        self.func(keycode, press)

    def escape(self, event):
        return event == None





t = TapRecord()
t.run()


class Clickonacci(PyMouseEvent):
    def __init__(self):
        PyMouseEvent.__init__(self)
    def click(self, x, y, button, press):
	  print(time.time(), button, press)
c = Clickonacci()
c.run()
