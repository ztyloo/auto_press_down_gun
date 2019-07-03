import threading
import os
import cv2
import numpy as np
from pykeyboard import PyKeyboardEvent
from PIL import ImageGrab

from auto_position_label.crop_position import screen_position_states
from show_watermark import Show_Watermark
from all_states import All_States


def get_screen():
    screen = ImageGrab.grab()
    screen = np.array(screen)
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    return screen


class Key_Listener(PyKeyboardEvent):
    def __init__(self, all_states):
        PyKeyboardEvent.__init__(self)
        root_path = 'D:/github_project/auto_press_down_gun/auto_position_label/screen_captures'

        self.all_states = all_states
        self.show = Show_Watermark()

        os.makedirs(root_path, exist_ok=True)
        for k, v in screen_position_states.items():
            if len(v) > 0:
                for state in v:
                    show
                    state_fold = os.path.join(root_path, state)
                    os.makedirs(state_fold, exist_ok=True)


    def tap(self, keycode, character, press):
        if keycode == 162 and press:  # ctrl
            screen = ImageGrab.grab()
            screen = np.array(screen)
            screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
            cv2.imwrite('ctrl_cap/' + str(self.i) + '.png', screen)
            self.i += 1

        if keycode == 164 and press:  # alt
            self.alt_func()


    def escape(self, event):
        return False

    def ctrl_func(self):
        pass

    def alt_func(self):
        pass




if __name__ == '__main__':
    all_from_dir = 'D:/github_project/auto_press_down_gun/auto_position_label/screen_captures/'
    all_to_dir = 'D:/github_project/auto_press_down_gun/image_detect/states_4c_im/'

    # screen_cap()
