import threading


class Press(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._loop = True

    def set_states(self, all_states):
        gun_n = all_states.weapon_n
        gun_name = all_states


    def run(self):
        pass

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
    pl = Press()
    pl.run()


import time
import win32api
import win32con
from threading import Timer
import pyautogui as pag



if __name__ == '__main__':
    i = 0
    x, y = pag.position()
    print(str(i) + ':', x, y)
    while True:
        i += 1
        time.sleep(1)
        mouse_down(20)
        x, y = pag.position()
        print(str(i) + ':', x, y)