

import threading
from threading import Thread

from conv_press_gun_test.my_timer import MyTimer
from conv_press_gun_test.press_down_distence import Down_distence
from conv_press_gun_test.press_utiles import *

class Auto_down():
    def __init__(self, k, b, max_x, x_interval, scope_time):
        super().__init__()
        self.max_x = max_x
        self.x_interval = x_interval
        self.dis = Down_distence(k, b, scope_time)
        self.timer = MyTimer(self.x_interval, self.timer_handler, 4)
        self.m_listener = Mouse_listern(self.click_handler)

    def timer_handler(self):
        print('down')
        down_dis = self.dis.pop()
        mouse_down(down_dis)
        print(time.time())

    def click_handler(self, x, y, button, press):
        if button == 1 and press:
            print(time.time())
            print('press')
            self.timer.start()

        if button == 1 and (not press):
            print('not press')
            self.dis.x = 0
            self.timer.cancel()
            self.dis.reset()

    def run(self):
        self.m_listener.run()

    def stop(self):
        self.m_listener.stop()


dp = Auto_down(0, 14, 30, 0.025, 1)

dp.run()