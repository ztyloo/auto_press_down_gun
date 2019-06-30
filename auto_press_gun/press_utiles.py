import time
import win32api
import win32con
from threading import Timer
import pyautogui as pag

#
# class RepeatingTimer(Timer):
#     def __init__(self, interval, function):
#         Timer.__init__(self, interval, function)
#         self._loop = True
#
#     def run(self):
#         while self._loop:
#
# t = RepeatingTimer(10.0, hello)
# t.start()
#
#
# def mouse_down_speed(y, t_ms):
#
#
#
def mouse_down(y):
    try:
        x = 0
        y = int(y)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y)
    except:
        print('Move Error')


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

