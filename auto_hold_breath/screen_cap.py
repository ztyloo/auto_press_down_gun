import time
import win32gui, win32ui, win32con, win32api
from pykeyboard import PyKeyboardEvent


def window_capture(rect, filename):
    x0, y0, x1, y1 = rect
    w, h = x1-x0, y1-y0

    hwnd = 0  # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((-x0, -y0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)


class Key_listener(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)
        self.i = 0

    def tap(self, keycode, character, press):

        if keycode == 162 and press:
            window_capture((-100, -100, 500, 500), str(self.i)+".png")
            self.i += 1

    def escape(self, event):
        return False


t = Key_listener()
t.run()


if __name__ == '__main__':
    # beg = time.time()
    # for i in range(10):
    #     window_capture((100, 100, 150, 150), str(i) + ".png")
    # end = time.time()
    # print(end - beg)

    kl = Key_listener()
    kl.run()

