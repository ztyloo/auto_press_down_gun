import threading
import cv2
import numpy as np
from pykeyboard import PyKeyboardEvent
from PIL import ImageGrab
import itchat

from image_detect.detect import Detector
from press_gun.press_listener import Press_Listener
from auto_position_label.crop_position import crop_screen, screen_position as sc_pos


def get_screen():
    screen = ImageGrab.grab()
    screen = np.array(screen)
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    return screen


class Key_Listener(PyKeyboardEvent):
    def __init__(self, all_states):
        PyKeyboardEvent.__init__(self)

        self.all_states = all_states

        self.fire_mode_detect = Detector('fire_mode')
        self.in_tab_detect = Detector('in_tab')
        self.in_scope_detect = Detector('in_scope')

        self.name_detect = Detector('name')
        self.scope_detect = Detector('scope')
        # self.muzzle_detect = Detector('muzzle')
        # self.grip_detect = Detector('grip')

        self.press_listener = None
        # itchat.auto_login(hotReload=True)
        # itchat.send('Initial done!!!')
        print('Initial done!!!')

    def tap(self, keycode, character, press):
        if keycode == 9 and press:  # tab
            threading.Timer(0.001, self.tab_func).start()

        if keycode == 123 and press:  # F12
            threading.Timer(0.001, self.whether_start_listen).start()

        if keycode == 71 and press:  # g
            threading.Timer(0.001, self.whether_start_listen).start()

        if keycode == 53 and press:  # 5
            threading.Timer(0.001, self.whether_start_listen).start()

        if keycode == 66 and press:  # b
            threading.Timer(0.2, self.b_func).start()

        if keycode == 49 and press:  # 1
            self.all_states.weapon_n = 0
            threading.Timer(0.001, self.whether_start_listen).start()

        if keycode == 50 and press:  # 2
            self.all_states.weapon_n = 1
            threading.Timer(0.001, self.whether_start_listen).start()

    def escape(self, event):
        return False

    def tab_func(self):
        self.stop_listen()

        screen = get_screen()
        if 'in' == self.in_tab_detect.diff_sum_classify(crop_screen(screen, sc_pos['in_tab'])):
            for n in [0, 1]:
                name_crop = crop_screen(screen, sc_pos['weapon'][str(n)]['name'])
                scope_crop = crop_screen(screen, sc_pos['weapon'][str(n)]['scope'])
                # muzzle_crop = crop_screen(screen, sc_pos['name'][str(n)]['muzzle'])
                # grip_crop = crop_screen(screen, sc_pos['name'][str(n)]['grip'])
                self.all_states.weapon[n].name = self.name_detect.diff_sum_classify(name_crop)
                self.all_states.weapon[n].scope = self.scope_detect.diff_sum_classify(scope_crop, absent_return="1")
                # self.all_states.name[n].muzzle = self.muzzle_detect.diff_sum_classify(muzzle_crop)
                # self.all_states.name[n].grip = self.grip_detect.diff_sum_classify(grip_crop)
            print_state(self.all_states)

        self.whether_start_listen()

    def b_func(self):
        self.stop_listen()

        screen = get_screen()
        fire_mode_crop = crop_screen(screen, sc_pos['fire_mode'])
        n = self.all_states.weapon_n
        self.all_states.weapon[n].fire_mode = self.fire_mode_detect.water_mark_classify(fire_mode_crop)

        print_state(self.all_states)
        self.whether_start_listen()

    def stop_listen(self):
        if self.press_listener is not None:
            self.press_listener.stop()

    def whether_start_listen(self):
        n = self.all_states.weapon_n
        if self.all_states.weapon[n].name != '' and self.all_states.weapon[n].fire_mode == 'full':
            if self.press_listener is not None:
                self.press_listener.stop()
            self.press_listener = Press_Listener(self.all_states)
            self.press_listener.start()


def print_state(all_states):
    print('now_weapon: ', str(all_states.weapon_n))
    for n in [0, 1]:
        w = all_states.weapon[n]
        print(str(w.name) + ' ' + str(w.scope) + ' ' + str(w.fire_mode))

    # itchat.send('\n')
    # itchat.send(print_str)

