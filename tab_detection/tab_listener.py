
from pykeyboard import PyKeyboardEvent


class Tab_Listener(PyKeyboardEvent):
    def __init__(self, func):
        PyKeyboardEvent.__init__(self)
        self.func = func

    def tap(self, keycode, character, press):
        if keycode == 190 and not press:
            self.func()

    def escape(self, event):
        return False


def test_user_name