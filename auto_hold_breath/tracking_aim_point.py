import threading
import win32api
import win32con
import time

from screen_capture import win32_cap
from auto_hold_breath.aim_point import Aim_Point


def mouse_move(dx, dy):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(dx), int(dy))


class Tracking_Aim_Point(threading.Thread):
    def __init__(self, scope):
        threading.Thread.__init__(self)
        self.scope = str(scope)
        self._loop = True
        self.aim_point = Aim_Point()

    def run(self) -> None:
        radius = 100
        temp_path = 'D:/github_project/auto_press_down_gun/auto_hold_breath/temp_fold/temp.png'
        im = win32_cap(temp_path, (1719 - radius, 719 - radius, 1719 + radius, 719 + radius))
        x0, y0 = self.aim_point.find(im, self.scope)
        i = 0
        while self._loop:
            radius = 100
            temp_path = 'D:/github_project/auto_press_down_gun/auto_hold_breath/temp_fold/'+str(i)+'.png'
            im = win32_cap(temp_path, (1719-radius, 719-radius,1719+radius, 719+radius))
            x1, y1 = self.aim_point.find(im, self.scope)
            dx, dy = x0 - x1, y0 - y1
            print(dx, dy)
            dx = dx if dx<10 else 0
            dy = dy if dy<10 else 0
            mouse_move(dx, dy)
            x0, y0 = x1, y1

            i = i+1 if i<20 else 0

    def stop(self):
        self._loop = False


if __name__ == '__main__':
    tracking_aim_point = Tracking_Aim_Point(6)
    tracking_aim_point.run()
