import threading
import cv2
import numpy as np
from pykeyboard import PyKeyboardEvent
from PIL import ImageGrab
from PyQt5.QtCore import pyqtSignal, QObject

from image_detect.detect import Detector
from press_gun.press_listener import Press_Listener
from auto_position_label.crop_position import crop_screen, screen_position as sc_pos
from all_states import All_States, gun_next_mode


class Temp_QObject(QObject):
    state_str_signal = pyqtSignal(str)


class All_Listener(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)

        self.all_states = All_States()
        self.mistake_counter = 0
        self.screen = None

        self.fire_mode_detect = Detector('fire_mode')
        self.in_tab_detect = Detector('in_tab')
        # self.in_scope_detect = Detector('in_scope')

        self.weapon1name_detect = Detector('weapon1name')
        self.weapon1scope_detect = Detector('weapon1scope')

        self.weapon2name_detect = Detector('weapon2name')
        self.weapon2scope_detect = Detector('weapon2scope')

        self.press_listener = Press_Listener(self.all_states)

        self.temp_qobject = Temp_QObject()
        print('Initial done!!!')

    def tap(self, keycode, character, press):
        if keycode == 9 and press:  # tab
            self.get_screen()
            threading.Timer(0.001, self.tab_func).start()
            self.print_state()

        if keycode == 123 and press:  # F12
            self.stop_listen()
            self.print_state()

        if keycode == 71 and press:  # g
            self.stop_listen()
            self.print_state()

        if keycode == 53 and press:  # 5
            self.stop_listen()
            self.print_state()

        if keycode == 66 and press:  # b
            self.stop_listen()
            threading.Timer(0.2, self.b_func).start()
            self.print_state()

        if keycode == 49 and press:  # 1
            self.all_states.weapon_n = 0
            self.whether_start_listen()
            self.print_state()

        if keycode == 50 and press:  # 2
            self.all_states.weapon_n = 1
            self.whether_start_listen()
            self.print_state()

    def escape(self, event):
        return False

    def tab_func(self):
        self.stop_listen()
        # cc = crop_screen(self.screen, sc_pos['in_tab'])
        # cv2.imwrite('cc.png', cc)
        if 'in' == self.in_tab_detect.diff_sum_classify(crop_screen(self.screen, sc_pos['in_tab'])):
            # cv2.imshow('screen', self.screen)
            # cv2.waitKey()

            weapon1name_crop = crop_screen(self.screen, sc_pos['weapon1name'])
            self.all_states.weapon[1].set_name(self.weapon1name_detect.diff_sum_classify(weapon1name_crop, check=True))
            weapon1scope_crop = crop_screen(self.screen, sc_pos['weapon1scope'])
            self.all_states.weapon[1].set_scope(self.weapon1scope_detect.diff_sum_classify(weapon1scope_crop, absent_return="1"))

            weapon2name_crop = crop_screen(self.screen, sc_pos['weapon2name'])
            self.all_states.weapon[2].set_name(self.weapon2name_detect.diff_sum_classify(weapon2name_crop))
            weapon2scope_crop = crop_screen(self.screen, sc_pos['weapon2scope'])
            self.all_states.weapon[2].set_scope(self.weapon2scope_detect.diff_sum_classify(weapon2scope_crop, absent_return="1"))

        self.whether_start_listen()

    def b_func(self):
        self.get_screen()

        n = self.all_states.weapon_n
        fire_mode_crop = crop_screen(self.screen, sc_pos['fire_mode'])
        pre_fire_mode = self.all_states.weapon[n].fire_mode
        self.all_states.weapon[n].set_fire_mode(self.fire_mode_detect.canny_classify(fire_mode_crop))

        # # check if mistake
        # if pre_fire_mode != '':
        #     next_fire_mode = gun_next_mode(self.all_states.weapon[n].name, pre_fire_mode)
        #     if next_fire_mode != self.all_states.weapon[n].fire_mode:
        #         root_path = 'D:/github_project/auto_press_down_gun/image_detect/temp_test_image/' + str(self.mistake_counter) + '.png'
        #         cv2.imwrite(root_path, self.screen)

        self.whether_start_listen()

    def stop_listen(self):
        if self.press_listener.is_alive():
            self.press_listener.stop()

    def whether_start_listen(self):
        if self.press_listener.is_alive():
            self.press_listener.stop()

        n = self.all_states.weapon_n
        if self.all_states.weapon[n].name != '' and self.all_states.weapon[n].fire_mode == 'full':
            self.press_listener = Press_Listener(self.all_states)
            self.press_listener.start()

    def print_state(self):
        n = self.all_states.weapon_n
        print('now_weapon: ', str(n))
        for i in [0, 1]:
            w = self.all_states.weapon[i]
            print(str(w.name) + '-' + str(w.scope) + '-' + str(w.fire_mode))

        w = self.all_states.weapon[0]
        gun1_state = str(w.name) + '-' + str(w.scope) + '-' + str(w.fire_mode)
        w = self.all_states.weapon[1]
        gun2_state = str(w.name) + '-' + str(w.scope) + '-' + str(w.fire_mode)
        emit_str = str(n)+ '  ' + gun1_state + '\n' + gun2_state
        self.temp_qobject.state_str_signal.emit(emit_str)

    def get_screen(self):
        screen = ImageGrab.grab()
        screen = np.array(screen)
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
        self.screen = screen


if __name__ == '__main__':
    k = All_Listener()
    k.run()
