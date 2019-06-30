from pykeyboard import PyKeyboardEvent, PyKeyboard
from auto_press_gun.my_timer import MyTimer
from auto_press_gun.press_down_distence import Down_distence
from auto_press_gun.press_utiles import *
from auto_press_gun.time_interval_constant import time_interval
from generate_distance.gun_distance_constant import dis_interval


class Auto_down:
    def __init__(self):
        self.no_start = True
        super().__init__()
        self.m_listener = Mouse_listern(self.click_handler)
        self.k = PyKeyboard()
        self.dis_interval_dict = dis_interval
        self.time_interval_dict = time_interval

    def reset(self, gun_name: str, scope: int):
        dis_list = self.dis_interval_dict[gun_name]
        self.dis = Down_distence(dis_list, scope)

        x_interval = self.time_interval_dict[gun_name]
        self.timer = MyTimer(x_interval, self.timer_handler)

    def timer_handler(self):
        # print('down')
        down_dis = self.dis.pop()
        mouse_down(down_dis)

    def click_handler(self, x, y, button, press):
        if button == 1 and press:
            self.k.press_key(160)
            self.timer.start()

        if button == 1 and (not press):
            self.k.release_key(160)
            self.dis.reset()
            self.timer.cancel()

    def m_listener_run(self):
        # print('press start')
        self.m_listener.run()

    def m_listener_stop(self):
        # print('press stop')
        self.m_listener.stop()
        self.m_listener = Mouse_listern(self.click_handler)


if __name__ == '__main__':

    ad = Auto_down()
    ad.reset('scar', 1)
    ad.m_listener_run()
