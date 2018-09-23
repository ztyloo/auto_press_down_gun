import cv2
import numpy as np


from PIL import ImageGrab
from pykeyboard import PyKeyboardEvent

from tab_detection.detect import Tab
from b_detection.fire_mode_detection import Bb
from auto_press_gun.press import Auto_down


class Key_Listener(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)
        self.t = Tab()
        self.b = Bb()
        self.ad = Auto_down()
        self.t_set = False

    def tap(self, keycode, character, press):
        if keycode == 9 and press:
            screen = self.get_screen()
            self.t.set_screen(screen)
            if self.t.test():
                self.ad.reset(self.t.gun_name, self.t.scope_time)
                self.t_set = True

        if keycode == 66 and not press and self.t_set:
            screen = self.get_screen()
            self.b.set_screen(screen)
            self.b.test()
            if self.b.mode == 'full':
                self.ad.start()
            else:
                print('stop press')
                self.ad.stop()
                self.ad = Auto_down()

    def get_screen(self):
        screen = ImageGrab.grab()
        screen = np.array(screen)
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)

        # screen = cv2.imread('')
        return screen

    def escape(self, event):
        return False

k = Key_Listener()
k.run()