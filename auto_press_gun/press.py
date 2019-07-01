import threading
import win32api
import win32con
import time

from auto_press_gun.time_interval_constant import time_intervals
from generate_distance.gun_distance_constant import dis_intervals


class Press(threading.Thread):
    def __init__(self, all_states):
        threading.Thread.__init__(self)
        self._loop = True

        self.set_states(all_states)

    def set_states(self, all_states):
        gun_n = all_states.weapon_n
        gun_name = all_states.weapon[gun_n].name
        gun_scope = int(all_states.weapon[gun_n].scope.replace('r', '').replace('h', ''))
        dis_interval = dis_intervals[gun_name]*gun_scope
        time_interval = time_intervals[gun_name]
        divide_num = int(time_interval/0.02)  # 整数分割

        self.time_sequence = list()
        self.dist_sequence = list()
        for dist in dis_interval:
            for i in range(divide_num):
                self.time_sequence.append(time_interval/divide_num)
                self.dist_sequence.append(dist/divide_num)
        self.seq_len = len(self.time_sequence)

    def run(self):
        i = 0
        while self._loop and i < self.seq_len:
            dt = self.time_sequence[i]
            dd = self.dist_sequence[i]
            mouse_down(dd)
            time.sleep(dt)
            i += 1

    def stop(self):
        self._loop = False


def mouse_down(y):
    try:
        x = 0
        y = int(y)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y)
    except:
        print('Move Error')


class Down_distence:
    def __init__(self, dis_list, tms):
        self.tms = tms
        self.x = 0
        self.dis_list = dis_list
        self.lenth = len(self.dis_list)

    def pop(self):
        if self.x < self.lenth:
            y = self.dis_list[self.x]
            self.x += 1
        else:
            y = 0
        return y*self.tms

    def reset(self):
        self.x = 0


if __name__ == '__main__':
    import pyautogui as pag
    i = 0
    x, y = pag.position()
    print(str(i) + ':', x, y)
    while True:
        i += 1
        time.sleep(1)
        mouse_down(20)
        x, y = pag.position()
        print(str(i) + ':', x, y)


    #
    # pl = Press()
    # pl.run()
