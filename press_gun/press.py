import threading
import win32api
import win32con
import time


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

