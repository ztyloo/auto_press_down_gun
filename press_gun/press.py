import threading
import win32api
import win32con
import time

from press_gun.time_interval_constant import time_intervals
from press_gun.generate_distance.gun_distance_constant import dis_intervals


# import pyautogui as pag
#     i = 0
#     x, y = pag.position()
#     print(str(i) + ':', x, y)
#     while True:
#         i += 1
#         time.sleep(1)
#         mouse_down(20)
#         x, y = pag.position()
#         print(str(i) + ':', x, y)


def factor_scope(scope):
    factor = 1
    if scope == 1:
        factor = 1.1
    if scope == 2:
        factor = 1.
    if scope == 3:
        factor = 1.
    if scope == 4:
        factor = 1.1
    if scope == 6:
        factor = 0.8
    return scope * factor


def calculate_press_seq(all_states):
    gun_n = all_states.weapon_n
    gun_name = all_states.weapon[gun_n].name
    gun_scope = int(all_states.weapon[gun_n].scope.replace('r', '').replace('h', ''))
    gun_scope = factor_scope(gun_scope)
    dis_interval = dis_intervals.get(gun_name, [])
    dis_interval = [i * gun_scope for i in dis_interval]
    time_interval = time_intervals.get(gun_name, 1)
    divide_num = int(time_interval/0.02)  # 整数分割

    time_sequence = list()
    dist_sequence = list()
    for dist in dis_interval:
        for i in range(divide_num):
            time_sequence.append(time_interval/divide_num)
            dist_sequence.append(dist/divide_num)

    return dist_sequence, time_sequence


class Press(threading.Thread):
    def __init__(self, dist_seq, time_seq):
        threading.Thread.__init__(self)
        self.dist_seq, self.time_seq = dist_seq, time_seq
        self._loop = True
        self.seq_len = len(self.dist_seq)

    def run(self):
        i = 0
        while self._loop and i < self.seq_len:
            dt = self.time_seq[i]
            dd = self.dist_seq[i]
            mouse_down(dd)
            time.sleep(dt)
            i += 1
        if i > 0:
            mouse_down(-self.dist_seq[i-1])

    def stop(self):
        self._loop = False


def mouse_down(y):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, int(y))


if __name__ == '__main__':
    pass

