from pymouse import PyMouseEvent
from pykeyboard import PyKeyboardEvent
import pyautogui as pag

class Mouse_listern(PyMouseEvent):
    def __init__(self):
        PyMouseEvent.__init__(self)

    def click(self, x, y, button, press):
        print(x, y, button, press)

    def move(self, x, y):
        print(x, y)


class TapRecord(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)
        self.first_tap = True

    def tap(self, keycode, character, press):
        # print(keycode, character, press)
        if keycode == 160 and press:
            if self.first_tap is True:
                x, y = pag.position()
                print('start:', x, y)
                self.first_tap = False

        if keycode == 160 and not press:
            x, y = pag.position()
            print('end:', x, y)
            self.first_tap = True



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



kl = TapRecord()
kl.run()

