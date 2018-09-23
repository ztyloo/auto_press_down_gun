from threading import Thread
import yaml
from pykeyboard import PyKeyboardEvent, PyKeyboard
from auto_press_gun.my_timer import MyTimer
from auto_press_gun.press_down_distence import Down_distence
from auto_press_gun.press_utiles import *

class Auto_down(Thread):
    def __init__(self):
        super().__init__()
        self.m_listener = Mouse_listern(self.click_handler)
        self.k = PyKeyboard()
        with open('../generate_distance/gun_distance.yaml', 'r') as f:
            self.dis_dict = yaml.load(f)
        with open('time_interval.yaml', 'r') as f:
            self.interval_dict = yaml.load(f)

    def reset(self, gun_name: str, scope: int):
        dis_list = self.dis_dict[gun_name]
        self.dis = Down_distence(dis_list, scope)

        x_interval = self.interval_dict[gun_name]
        self.timer = MyTimer(x_interval, self.timer_handler)

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

    ad = Auto_down()
    ad.reset('scar', 1)
    ad.run()
