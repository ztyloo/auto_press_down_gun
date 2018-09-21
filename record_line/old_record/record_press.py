import time
import win32api
import win32con
from pymouse import PyMouseEvent
from pymouse import PyMouse
import pyautogui as pag

m = PyMouse()
def mouse_move_rel(dx,dy):#Move Postion
    try:
        dx = int(dx)
        dy = int(dy)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy)

        # x, y = m.position()
        # x = x + dy
        # y = y + dy
        # m.move(x, y)

    except:
        print('Move Error')


def mouse_down(y):
    try:
        x = 0
        y = int(y)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y)
    except:
        print('Move Error')