import threading
import cv2
import numpy as np
from pykeyboard import PyKeyboardEvent
from PyQt5.QtCore import pyqtSignal, QObject

from image_detect.detect import Detector
from auto_position_label.crop_position import screen_position
from all_states import All_States, gun_next_mode
from press_gun.press import Press
from screen_capture import win32_cap


class Temp_QObject(QObject):
    state_str_signal = pyqtSignal(str)


class Key_Listener(PyKeyboardEvent):
    def __init__(self, all_states):
        PyKeyboardEvent.__init__(self)

        self.all_states = all_states
        self.mistake_counter = 0
        self.screen = None

        self.fire_mode_detect = Detector('fire_mode')
        self.in_tab_detect = Detector('in_tab')
        # self.in_scope_detect = Detector('in_scope')

        self.weapon1name_detect = Detector('weapon1name')
        self.weapon1scope_detect = Detector('weapon1scope')
        self.weapon1muzzle_detect = Detector('weapon1muzzle')
        self.weapon1grip_detect = Detector('weapon1grip')
        self.weapon1butt_detect = Detector('weapon1butt')

        self.weapon2name_detect = Detector('weapon2name')
        self.weapon2scope_detect = Detector('weapon2scope')
        self.weapon2muzzle_detect = Detector('weapon2muzzle')
        self.weapon2grip_detect = Detector('weapon2grip')
        self.weapon2butt_detect = Detector('weapon2butt')

        self.temp_qobject = Temp_QObject()

    def tap(self, keycode, character, press):
        if keycode == 9 and press:  # tab
            threading.Timer(0.001, self.tab_func).start()

        if keycode == 66 and press:  # b
            self.all_states.dont_press = False
            threading.Timer(0.2, self.b_func).start()

        if keycode == 49 and press:  # 1
            n_change = self.all_states.set_weapon_n(0)
            if n_change:
                self.print_state()

        if keycode == 50 and press:  # 2
            n_change = self.all_states.set_weapon_n(1)
            if n_change:
                self.print_state()

        if keycode == 71 and press:  # g
            self.all_states.dont_press = True

        if keycode == 119 and press:  # F8
            self.all_states.dont_press = True

        if keycode == 122 and press:  # F11
            if not self.all_states.dont_press:
                n = self.all_states.weapon_n
                self.press = Press(self.all_states.weapon[n].dist_seq, self.all_states.weapon[n].time_seq)
                self.press.start()

        if keycode == 123 and not press:  # F12
            if not self.all_states.dont_press:
                if self.press.is_alive():
                    self.press.stop()

    def escape(self, event):
        return False

    def tab_func(self):
        self.all_states.dont_press = True
        if 'in' == self.in_tab_detect.diff_sum_classify(get_screen('in_tab')):
            self.all_states.dont_press = False

            crop = get_screen('weapon1name')
            res = self.weapon1name_detect.diff_sum_classify(crop)
            w1n_change = self.all_states.weapon[0].set_name(res)

            crop = get_screen('weapon1scope')
            res = self.weapon1scope_detect.diff_sum_classify(crop, absent_return="1")
            w1s_change = self.all_states.weapon[0].set_scope(res)

            crop = get_screen('weapon1muzzle')
            res = self.weapon1muzzle_detect.diff_sum_classify(crop)
            w1m_change = self.all_states.weapon[0].set_scope(res)

            crop = get_screen('weapon1grip')
            res = self.weapon1grip_detect.diff_sum_classify(crop)
            w1g_change = self.all_states.weapon[0].set_scope(res)

            crop = get_screen('weapon1butt')
            res = self.weapon1butt_detect.diff_sum_classify(crop)
            w1b_change = self.all_states.weapon[0].set_scope(res)

            if w1n_change or w1s_change or w1m_change or w1g_change or w1b_change:
                self.all_states.weapon[0].set_seq()

            crop = get_screen('weapon2name')
            res = self.weapon2name_detect.diff_sum_classify(crop)
            w2n_change = self.all_states.weapon[1].set_name(res)

            crop = get_screen('weapon2scope')
            res = self.weapon2scope_detect.diff_sum_classify(crop, absent_return="1")
            w2s_change = self.all_states.weapon[1].set_scope(res)

            crop = get_screen('weapon2muzzle')
            res = self.weapon2muzzle_detect.diff_sum_classify(crop)
            w2m_change = self.all_states.weapon[1].set_scope(res)

            crop = get_screen('weapon2grip')
            res = self.weapon2grip_detect.diff_sum_classify(crop)
            w2g_change = self.all_states.weapon[1].set_scope(res)

            crop = get_screen('weapon2butt')
            res = self.weapon2butt_detect.diff_sum_classify(crop)
            w2b_change = self.all_states.weapon[1].set_scope(res)

            if w2n_change or w2s_change or w2m_change or w2g_change or w2b_change:
                self.all_states.weapon[1].set_seq()

            if w1n_change or w1s_change or w2n_change or w2s_change:
                self.print_state()

    def b_func(self):
        fire_mode_crop = get_screen('fire_mode')
        fire_mode = self.fire_mode_detect.canny_classify(fire_mode_crop)
        n = self.all_states.weapon_n
        fm_change =  self.all_states.weapon[n].set_fire_mode(fire_mode)
        if fm_change:
            self.print_state()

    def print_state(self):
        n = self.all_states.weapon_n
        w = self.all_states.weapon[0]
        gun1_state = str(w.name) + '-' + str(w.scope) + '-' + str(w.fire_mode)
        w = self.all_states.weapon[1]
        gun2_state = str(w.name) + '-' + str(w.scope) + '-' + str(w.fire_mode)
        if n == 0:
            emit_str = ' * ' + gun1_state + '\n' + gun2_state
        else:
            emit_str = gun1_state + '\n' + ' * ' + gun2_state

        print('----------------')
        print(emit_str)
        self.temp_qobject.state_str_signal.emit(emit_str)


def get_screen(name):
    pos = screen_position[name]
    temp_fold = 'D:/github_project/auto_press_down_gun/press_gun/temp_image/'
    im = win32_cap(temp_fold + name + '.png', pos)
    return im


if __name__ == '__main__':
    all_states = All_States()
    k = Key_Listener(all_states)
    k.run()
