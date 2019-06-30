import time
import win32api
import win32con
from pymouse import PyMouseEvent
from pymouse import PyMouse
import pyautogui as pag


def mouse_move_rel(x,y):#Move Postion
    try:
        x = int(x)
        y = int(y)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y)
    except:
        print('Move Error')


def mouse_down(y):
    try:
        x = 0
        y = int(y)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y)
    except:
        print('Move Error')


# def mouse_down_(dy):
#     m = PyMouse()
#     x, y = m.position()
#     print(x, y)
#     y = y + dy
#     m.move(x, y)


class Mouse_listern(PyMouseEvent):
    def __init__(self, click_handler):
        PyMouseEvent.__init__(self)
        self.click_handler = click_handler

    def click(self, x, y, button, press):
        self.click_handler(x, y, button, press)


if __name__ == '__main__':
    i = 0
    x, y = pag.position()
    print(str(i) + ':', x, y)
    while True:
        i += 1
        time.sleep(1)
        mouse_down(5 )
        x, y = pag.position()
        print(str(i) + ':', x, y)