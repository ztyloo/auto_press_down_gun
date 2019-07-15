import time
import random
import cv2
import win32gui, win32ui, win32con, win32api
from pykeyboard import PyKeyboardEvent


def win32_cap(filename=None, rect=None):
    if filename == None:
        i = random.randrange(1, 1000)
        filename = 'D:/github_project/auto_press_down_gun/temp_image/'+str(i) + '.png'

    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    x0, y0 = 0, 0
    if rect is not None:
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
    # 截取从左上角(x0, y0)长宽为(w, h)的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (x0, y0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)
    im = cv2.imread(filename)
    return im


class Key_listener(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)
        self.i = 0

    def tap(self, keycode, character, press):

        if keycode == 162 and press:
            win32_cap('ctrl_cap/' + str(self.i)+".png")
            self.i += 1

    def escape(self, event):
        return False


if __name__ == '__main__':
    # beg = time.time()
    # for i in range(10):
    #     win32_cap((100, 100, 500, 500), str(i) + ".png")
    # end = time.time()
    # print(end - beg)

    kl = Key_listener()
    kl.run()

