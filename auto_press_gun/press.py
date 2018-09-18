import threading
from threading import Thread

from auto_press_gun.my_timer import MyTimer
from auto_press_gun.press_down_distence import Down_distence
from auto_press_gun.press_utiles import *

class Auto_down(Thread):
    def __init__(self, max_x, x_interval, scope_time):
        super().__init__()
        self.max_x = max_x
        self.x_interval = x_interval
        self.dis = Down_distence(scope_time)
        self.timer = MyTimer(self.x_interval, self.timer_handler)
        self.m_listener = Mouse_listern(self.click_handler)

    def timer_handler(self):
        print('down')
        down_dis = self.dis.pop()
        mouse_down(down_dis)

    def click_handler(self, x, y, button, press):
        if button == 1 and press:
            print('press')
            self.timer.start()

        if button == 1 and (not press):
            print('not press')
            self.dis.reset()
            self.timer.cancel()

    def run(self):
        self.m_listener.run()

    def stop(self):
        self.m_listener.stop()


dp = Auto_down(30, 0.125, 1)

dp.run()
print('-----------------')
dp.stop()
print('====================')