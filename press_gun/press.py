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
    def __init__(self, dist_sequence, time_sequence):
        threading.Thread.__init__(self)
        self._loop = True
        self.dist_sequence = dist_sequence
        self.time_sequence = time_sequence
        self.seq_len = len(dist_sequence)

    def run(self):
        i = 0
        while self._loop and i < self.seq_len:
            dt = self.time_sequence[i]
            dd = self.dist_sequence[i]
            mouse_down(dd)
            time.sleep(dt)
            i += 1
        # mouse_down(-self.dist_sequence[i])

    def stop(self):
        print('in stop')
        self._loop = False
        print('go out stop')


def mouse_down(y):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, int(y))


if __name__ == '__main__':
    pass

