import threading
import cv2
import numpy as np
from pymouse import PyMouseEvent
from pykeyboard import PyKeyboardEvent
from PIL import ImageGrab
import itchat

from auto_press_gun.press import Auto_down
from lists import *
from image_detect.detect import Detector


def get_screen():
    screen = ImageGrab.grab()
    screen = np.array(screen)
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    return screen

class Key_Listener(PyKeyboardEvent):
    def __init__(self, all_states):
        PyKeyboardEvent.__init__(self)

        self.all_states = all_states

        self.fire_mode_detect = Detector('fire_mode', 'fire_mode')
        self.in_tab_detect = Detector('in_tab', 'in_tab')
        self.in_scope_detect = Detector('in_scope', 'in_scope')

        self.weapon_1_detect = Detector('weapon_1', 'weapon')
        self.scope_1_detect = Detector('scope_1', 'scope')
        # self.muzzle_1_detect = Detector('muzzle_1', 'muzzle')
        # self.grip_1_detect = Detector('grip_1', 'grip')

        self.weapon_2_detect = Detector('weapon_2', 'weapon')
        self.scope_2_detect = Detector('2', 'scope')
        # self.muzzle_2_detect = Detector('muzzle_2', 'muzzle')
        # self.grip_2_detect = Detector('grip_2', 'grip')

        self.ad = Auto_down()
        itchat.auto_login(hotReload=True)
        print('Initial done!!!')

    def tap(self, keycode, character, press):
        if keycode == 9 and press:  # tab
            threading.Timer(0.001, self.tab_func).start()

        if keycode == 123 and press:  # F12
            threading.Timer(0.001, self.f12_func).start()

        if keycode == 71 and press:  # g
            threading.Timer(0.001, self.ad_stop_func).start()

        if keycode == 53 and press:  # 5
            threading.Timer(0.001, self.ad_stop_func).start()

        if keycode == 66 and press:  # b
            threading.Timer(0.001, self.b_func).start()

        if keycode == 49 and press:  # 1
            self.all_states.now_weapon = 1
            threading.Timer(0.001, self.set_auto_down).start()

        if keycode == 50 and press:  # 2
            self.all_states.now_weapon = 2
            threading.Timer(0.001, self.set_auto_down).start()

    def escape(self, event):
        return False

    def tab_func(self):
        self.all_states.in_tab = False
        self.ad.m_listener_stop()
        screen = get_screen()
        if 'in' == self.in_tab_detect.diff_sum_classify(screen):
            self.all_states.in_tab = True

            self.all_states.weapon_1 = self.weapon_1_detect.diff_sum_classify(screen)
            scope_res = self.scope_1_detect.diff_sum_classify(screen)
            self.all_states.scope_1 = 1 if scope_res is None else int(scope_res[0])
            # self.all_states.muzzle_1 = self.muzzle_1_detect(screen)
            # self.all_states.grip_1 = self.grip_1_detect(screen)

            self.all_states.weapon_2 = self.weapon_2_detect.diff_sum_classify(screen)
            scope_res = self.scope_2_detect.diff_sum_classify(screen)
            self.all_states.scope_2 = 1 if scope_res is None else int(scope_res[0])
            # self.all_states.muzzle_2 = self.muzzle_2_detect(screen)
            # self.all_states.grip_2 = self.grip_2_detect(screen)

            if self.all_states.now_weapon == 1:
                print(self.all_states.weapon_1, self.all_states.scope_1, self.all_states.fire_mode_1)
                itchat.send(str(self.all_states.weapon_1)+' '+str(self.all_states.scope_1)+' '+str(self.all_states.fire_mode_1))
            else:
                print(self.all_states.weapon_2, self.all_states.scope_2, self.all_states.fire_mode_2)
                itchat.send(str(self.all_states.weapon_2)+' '+str(self.all_states.scope_2)+' '+str(self.all_states.fire_mode_2))

            self.set_auto_down()

    def b_func(self):
        self.ad.m_listener_stop()

        # if self.all_states.now_weapon == 1:
        #     if self.all_states.weapon_1 in two_state_list:
        #         if self.all_states.fire_mode_1 == 'full':
        #             self.all_states.fire_mode_1 = 'single'
        #         elif self.all_states.fire_mode_1 == 'single':
        #             self.all_states.fire_mode_1 = 'full'
        #     elif self.all_states.weapon_1 in three_state_list:
        #         if self.all_states.fire_mode_1 == 'full':
        #             self.all_states.fire_mode_1 = 'single'
        #         elif self.all_states.fire_mode_1 == 'single':
        #             self.all_states.fire_mode_1 = 'burst'
        #         elif self.all_states.fire_mode_1 == 'burst':
        #             self.all_states.fire_mode_1 = 'full'
        #     else:
        #         print('wrong state1')
        # elif self.all_states.now_weapon == 2:
        #     if self.all_states.weapon_2 in two_state_list:
        #         if self.all_states.fire_mode_2 == 'full':
        #             self.all_states.fire_mode_2 = 'single'
        #         elif self.all_states.fire_mode_2 == 'single':
        #             self.all_states.fire_mode_2 = 'full'
        #     elif self.all_states.weapon_2 in three_state_list:
        #         if self.all_states.fire_mode_2 == 'full':
        #             self.all_states.fire_mode_2 = 'single'
        #         elif self.all_states.fire_mode_2 == 'single':
        #             self.all_states.fire_mode_2 = 'burst'
        #         elif self.all_states.fire_mode_2 == 'burst':
        #             self.all_states.fire_mode_2 = 'full'
        #     else:
        #         print('wrong state2')

        # self.set_auto_down()

        screen = get_screen()
        if self.all_states.now_weapon == 1:
            self.all_states.fire_mode_1 = self.fire_mode_detect.water_mark_classify(screen)
        elif self.all_states.now_weapon == 2:
            self.all_states.fire_mode_2 = self.fire_mode_detect.water_mark_classify(screen)
        else:
            raise Exception('now_weapon error')
        self.set_auto_down()

        if self.all_states.now_weapon == 1:
            print(self.all_states.weapon_1, self.all_states.scope_1, self.all_states.fire_mode_1)
            itchat.send(str(self.all_states.weapon_1)+' '+str(self.all_states.scope_1)+' '+str(self.all_states.fire_mode_1))
        else:
            print(self.all_states.weapon_2, self.all_states.scope_2, self.all_states.fire_mode_2)
            itchat.send(str(self.all_states.weapon_2)+' '+str(self.all_states.scope_2)+' '+str(self.all_states.fire_mode_2))

    def ad_stop_func(self):
        self.ad.m_listener_stop()

    def f12_func(self):
        self.ad.m_listener_stop()
        self.all_states.fire_mode_1 = 'single'
        self.all_states.fire_mode_2 = 'single'

    def set_auto_down(self):
        if self.all_states.now_weapon == 1:
            if self.all_states.weapon_1 in full_mode_gun and self.all_states.fire_mode_1 == 'full':
                self.ad.reset(self.all_states.weapon_1, self.all_states.scope_1)
                self.ad.m_listener_run()
            else:
                self.ad.m_listener_stop()
        elif self.all_states.now_weapon == 2:
            if self.all_states.weapon_2 in full_mode_gun and self.all_states.fire_mode_2 == 'full':
                self.ad.reset(self.all_states.weapon_2, self.all_states.scope_2)
                self.ad.m_listener_run()
            else:
                self.ad.m_listener_stop()
        else:
            raise Exception('now_weapon error')


class Mouse_listern(PyMouseEvent):
    def __init__(self, all_states):
        PyMouseEvent.__init__(self)
        self.all_states = all_states

        self.fire_mode_detect = Detector('fire_mode', 'fire_mode')

    def click(self, x, y, button, press):
        if button == 2 and not press:
            threading.Timer(0.001, self.right_click).start()

    def right_click(self):
        pass
        # self.all_states


