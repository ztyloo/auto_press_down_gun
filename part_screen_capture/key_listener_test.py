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
        print(time.time(), keycode, character, press)

    def escape(self, event):
        """
        A function that defines when to stop listening; subclass this with your
        escape behavior. If the program is meant to stop, this method should
        return True. Every key event will go through this method before going to
        tap(), allowing this method to check for exit conditions.
        The default behavior is to stop when the 'Esc' key is pressed.
        If one wishes to use key combinations, or key series, one might be
        interested in reading about Finite State Machines.
        http://en.wikipedia.org/wiki/Deterministic_finite_automaton
        """
        condition = None
        return event == condition





t = TapRecord()
t.run()


class Clickonacci(PyMouseEvent):
    def __init__(self):
        PyMouseEvent.__init__(self)
    def click(self, x, y, button, press):
	  print(time.time(), button, press)
c = Clickonacci()
c.run()
