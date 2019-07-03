import threading
import os
import cv2
import numpy as np
from pykeyboard import PyKeyboardEvent
from PIL import ImageGrab

from auto_position_label.crop_position import screen_position_states
from show_watermark import Show_Watermark


def get_screen():
    screen = ImageGrab.grab()
    screen = np.array(screen)
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    return screen


class Key_Listener(PyKeyboardEvent):
    def __init__(self, all_states):
        PyKeyboardEvent.__init__(self)
        root_path = 'D:/github_project/auto_press_down_gun/auto_position_label/screen_captures'
        os.makedirs(root_path, exist_ok=True)

        self.path_strs = list()
        self.escape_c = '/'
        for k, v in screen_position_states.items():
            if len(v) > 0:
                for state in v:
                    state_fold = os.path.join(root_path, state)
                    os.makedirs(state_fold, exist_ok=True)

                    self.path_strs.append(k + self.escape_c + state)

        self.state_num = len(self.path_strs)
        self.all_states = all_states
        self.show = Show_Watermark()


    def tap(self, keycode, character, press):
        if keycode == 162 and press:  # ctrl
            self.alt_func()

        if keycode == 37 and press:  # <-
            self.left_func()

        if keycode == 39 and press:  # ->
            self.right_func()

        if keycode == 164 and press:  # alt
            self.alt_func()


    def escape(self, event):
        return False

    def ctrl_func(self):
        pass

    def left_func(self):
        pass

    def right_func(self):
        pass

    def alt_func(self):
        pass




if __name__ == '__main__':
    from all_states import All_States

    screen_cap_listener = Key_Listener(All_States())
