import threading
import cv2
import numpy as np
from pykeyboard import PyKeyboardEvent
from PIL import ImageGrab
from PyQt5.QtCore import pyqtSignal, QObject

from image_detect.detect import Detector
from auto_position_label.crop_position import crop_screen, screen_position as sc_pos
from all_states import All_States, gun_next_mode
from press_gun.press import Press


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

        self.weapon2name_detect = Detector('weapon2name')
        self.weapon2scope_detect = Detector('weapon2scope')

        self.temp_qobject = Temp_QObject()

    def tap(self, keycode, character, press):
        if keycode == 9 and press:  # tab
            self.get_screen()
            threading.Timer(0.001, self.tab_func).start()

        if keycode == 66 and press:  # b
            threading.Timer(0.2, self.b_func).start()

        if keycode == 49 and press:  # 1
            n_change = self.all_states.set_weapon_n(0)
            if n_change:
                self.print_state()

        if keycode == 50 and press:  # 2
            n_change = self.all_states.set_weapon_n(1)
            if n_change:
                self.print_state()

        if keycode == 122 and press:  # F11
            n = self.all_states.weapon_n
            self.press = Press(self.all_states.weapon[n].dist_seq, self.all_states.weapon[n].time_seq)
            self.press.start()

        if keycode == 123 and not press:  # F12
            self.press.stop()

    def escape(self, event):
        return False

    def tab_func(self):
        if 'in' == self.in_tab_detect.diff_sum_classify(crop_screen(self.screen, sc_pos['in_tab'])):
            # cv2.imshow('screen', self.screen)
            # cv2.waitKey()

            weapon1scope_crop = crop_screen(self.screen, sc_pos['weapon1scope'])
            weapon1scope = self.weapon1scope_detect.diff_sum_classify(weapon1scope_crop, absent_return="1")
            w1s_change = self.all_states.weapon[0].set_scope(weapon1scope)

            weapon1name_crop = crop_screen(self.screen, sc_pos['weapon1name'])
            weapon1name = self.weapon1name_detect.diff_sum_classify(weapon1name_crop, check=True)
            w1n_change = self.all_states.weapon[0].set_name(weapon1name)

            weapon2scope_crop = crop_screen(self.screen, sc_pos['weapon2scope'])
            weapon2scope = self.weapon2scope_detect.diff_sum_classify(weapon2scope_crop, absent_return="1")
            w2s_change = self.all_states.weapon[1].set_scope(weapon2scope)

            weapon2name_crop = crop_screen(self.screen, sc_pos['weapon2name'])
            weapon2name = self.weapon2name_detect.diff_sum_classify(weapon2name_crop)
            w2n_change = self.all_states.weapon[1].set_name(weapon2name)


            if w1n_change or w1s_change or w2n_change or w2s_change:
                self.print_state()

    def b_func(self):
        self.get_screen()

        n = self.all_states.weapon_n
        fire_mode_crop = crop_screen(self.screen, sc_pos['fire_mode'])
        fire_mode = self.fire_mode_detect.canny_classify(fire_mode_crop)
        fm_change =  self.all_states.weapon[n].set_fire_mode(fire_mode)
        if fm_change:
            self.print_state()

    def get_screen(self):
        screen = ImageGrab.grab()
        screen = np.array(screen)
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
        self.screen = screen

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


if __name__ == '__main__':
    all_states = All_States()
    k = Key_Listener(all_states)
    k.run()
