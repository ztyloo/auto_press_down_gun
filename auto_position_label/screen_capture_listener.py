import os
import cv2
import numpy as np
from pykeyboard import PyKeyboardEvent
from PIL import ImageGrab
from PyQt5.QtCore import pyqtSignal, QObject

from auto_position_label.crop_position import screen_position_states


def get_screen():
    screen = ImageGrab.grab()
    screen = np.array(screen)
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    return screen


class Temp_QObject(QObject):
    state_str_signal = pyqtSignal(str)


class Key_Listener(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)
        self.root_path = 'D:/github_project/auto_press_down_gun/auto_position_label/screen_captures'
        os.makedirs(self.root_path, exist_ok=True)

        self.state_folds = list()
        self.escape_c = '-'
        for k, v in screen_position_states.items():
            if len(v) > 0:
                for state in v:
                    self.state_folds.append(k + self.escape_c + state)

        self.state_n_max = len(self.state_folds) - 1
        self.state_n = 0
        self.im_n = 0

        self.temp_qobject = Temp_QObject()

    def init_show(self):
        self.print_state()

    def tap(self, keycode, character, press):
        if keycode == 162 and press:  # ctrl
            self.ctrl_func()
            self.print_state()

        if keycode == 37 and press:  # <-
            self.left_func()
            self.print_state()

        if keycode == 38 and press:  # up
            self.up_func()
            self.print_state()

        if keycode == 39 and press:  # ->
            self.right_func()
            self.print_state()

        if keycode == 40 and press:  # down
            self.down_func()
            self.print_state()

        if keycode == 164 and press:  # alt
            self.alt_func()
            self.print_state()

    def escape(self, event):
        return False

    def ctrl_func(self):
        screen = get_screen()

        save_fold = os.path.join(self.root_path, self.state_folds[self.state_n])
        os.makedirs(save_fold, exist_ok=True)
        save_path = os.path.join(save_fold, str(self.im_n)+'.png')
        cv2.imwrite(save_path, screen)

        self.im_n += 1

    def left_func(self):
        self.im_n = 0
        if self.state_n > 0:
            self.state_n -= 1

    def up_func(self):
        self.im_n += 1

    def right_func(self):
        self.im_n = 0
        if self.state_n < self.state_n_max:
            self.state_n += 1

    def down_func(self):
        self.im_n -= 1

    def alt_func(self):
        pass

    def print_state(self):
        emit_str = self.state_folds[self.state_n] + ' ' + str(self.im_n)+'.png'
        self.temp_qobject.state_str_signal.emit(emit_str)
        print('emit-->', emit_str)


if __name__ == '__main__':
    screen_cap_listener = Key_Listener()
