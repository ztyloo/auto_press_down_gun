import cv2
import numpy as np
from PIL import ImageGrab
from pykeyboard import PyKeyboardEvent


# if len(os.listdir('cap')) == 0:
#     i = 0
# else:
#     i = max(os.listdir('cap'), key=lambda x: int(x[:-4]))
#     i = int(i[:-4])


class Key_listener(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)
        self.i = 0

    def tap(self, keycode, character, press):

        if keycode == 162 and press:
            screen = ImageGrab.grab()
            screen = np.array(screen)
            screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
            cv2.imwrite('ctrl_cap/' + str(self.i) + '.png', screen)
            self.i += 1

            print(keycode, press)

    def escape(self, event):
        return False


t = Key_listener()
t.run()