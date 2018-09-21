from pymouse import PyMouseEvent
from pykeyboard import PyKeyboardEvent, PyKeyboard

from record_line.find_point import Find
from record_line.old_record.record_press import mouse_move_rel


class Mouse_listern(PyMouseEvent):
    def __init__(self):
        PyMouseEvent.__init__(self)

    def click(self, x, y, button, press):
        print(x, y, button, press)

    def move(self, x, y):
        print(x, y)


class Key_listern(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)
        self.first_tap = True
        self.res_list = []
        self.f = Find()
        self.epoch = 0
        self.num = 0
        self.k = PyKeyboard()

    def tap(self, keycode, character, press):
        if keycode == 57 and press:
            if self.num == 0:
                self.k.press_key(160)
                x0, y0 = 1719, 719
                x1, y1 = self.f.find_upper(self.epoch, self.num)
                dx = x1 - x0
                dy = y1 - y0
                dx = dx/2
                dy = dy/2
                mouse_move_rel(dx, dy)
                self.k.release_key(160)
            else:
                self.k.press_key(160)
                x0, y0 = 1719, 719
                x1, y1 = self.f.find_upper(self.epoch, self.num)
                dx = x1 - x0
                dy = y1 - y0
                dx = dx/2
                dy = dy/2
                mouse_move_rel(dx, dy)
                self.res_list.append((dx, dy))
                self.k.release_key(160)
            self.num += 1

        if keycode == 48 and press:
            self.num = 0
            self.epoch += 1
            print(self.res_list)
            self.res_list = []

    # def escape(self, event):
    #     condition = None
    #     return event == condition


if __name__ == '__main__':
    kl = Key_listern()
    kl.run()




    # k = PyKeyboard()
    # k.press_key(160)
    # time.sleep(5)
    # k.release_key(160)
    # time.sleep(5)

    # kl = Key_listern()
    # kl.run()

