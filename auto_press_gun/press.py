import threading

from auto_press_gun.my_timer import MyTimer
from auto_press_gun.press_down_distence import Down_distence
from auto_press_gun.press_utiles import *


class Auto_down:
    def __init__(self, k, b, max_x, x_interval, scope_time):
        self.max_x = max_x
        self.x_interval = x_interval
        self.dis = Down_distence(k, b, scope_time)
        self.timer = MyTimer(self.x_interval, self.timer_handler, self.max_x)
        self.m_listener = Mouse_listern(self.click_handler)
        self.m_listener.run()

    def timer_handler(self):
        print('down')
        down_dis = self.dis.pop()
        mouse_down(down_dis)

    def click_handler(self, x, y, button, press):
        if button == 1 and press:
            print('press')
            self.timer = MyTimer(self.x_interval, self.timer_handler, self.max_x)
            self.timer.start()

        if button == 1 and (not press):
            print('not press')
            self.dis.x = 0
            self.timer.cancel()

        if button == 2:
            self.timer.cancel()



dp = Auto_down(1, 25, 30, 0.1, 6)

