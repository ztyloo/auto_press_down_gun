import threading
from threading import Thread
import yaml
from pykeyboard import PyKeyboardEvent, PyKeyboard
from auto_press_gun.my_timer import MyTimer
from auto_press_gun.press_down_distence import Down_distence
from auto_press_gun.press_utiles import *

class Auto_down(Thread):
    def __init__(self, dis, x_interval):
        super().__init__()
        self.dis = dis
        self.timer = MyTimer(x_interval, self.timer_handler)
        self.m_listener = Mouse_listern(self.click_handler)
        self.k = PyKeyboard()

    def timer_handler(self):
        print('down')
        down_dis = self.dis.pop()
        mouse_down(down_dis)

    def click_handler(self, x, y, button, press):
        if button == 1 and press:
            self.k.press_key(160)
            print('press')
            self.timer.start()

        if button == 1 and (not press):
            self.k.release_key(160)
            print('not press')
            self.dis.reset()
            self.timer.cancel()

    def run(self):
        self.m_listener.run()

    def stop(self):
        self.m_listener.stop()


if __name__ == '__main__':
    gun_name = 'scal'

    with open('press_distance.yaml', 'r') as f:
        yaml_dis = yaml.load(f)
        dis_list = yaml_dis[gun_name]
    with open('time_interval.yaml', 'r') as f:
        yaml_time_interval = yaml.load(f)
        time_interval = yaml_time_interval[gun_name]

    dis = Down_distence(dis_list, 6.)
    dp = Auto_down(dis, time_interval)




    dp.run()
    print('-----------------')
    dp.stop()
    print('====================')