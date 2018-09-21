import time
import win32gui, win32ui, win32con, win32api


class Screen:
    def __init__(self):
        hdesktop = win32gui.GetDesktopWindow()
        self.desktop_dc = win32gui.GetWindowDC(hdesktop)

        self.top = 670
        self.left = 1715
        self.w = 10
        self.h = 50

        self.dc_list = []
        self.bitmap_list = []

    def shot(self):
        img_dc = win32ui.CreateDCFromHandle(self.desktop_dc)
        mem_dc = img_dc.CreateCompatibleDC()

        bitmap = win32ui.CreateBitmap()
        # 创建位图对象
        bitmap.CreateCompatibleBitmap(img_dc, self.w, self.h)
        mem_dc.SelectObject(bitmap)

        # 截图至内存设备描述表
        mem_dc.BitBlt((0, 0), (self.w, self.h), img_dc, (self.left, self.top), win32con.SRCCOPY)
        self.dc_list.append(mem_dc)
        self.bitmap_list.append(bitmap)

    def save(self, dir):
        for i, (dc, bitmap) in enumerate(zip(self.dc_list, self.bitmap_list)):
            bitmap.SaveBitmapFile(dc, dir + str(i) + '.png')
            dc.DeleteDC()
            win32gui.DeleteObject(bitmap.GetHandle())


if __name__ == '__main__':
    time.sleep(10)
    sc = Screen()

    t0 = time.time()
    for i in range(20):
        time.sleep(1)
        sc.shot()
    t1 = time.time()
    print(t1-t0)
    sc.save('screens/')