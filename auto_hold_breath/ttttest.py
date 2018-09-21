# 截图整个桌面
import time
import win32gui
import win32ui
import win32con
import win32api

# 获取桌面
hdesktop = win32gui.GetDesktopWindow()

top = 670
left = 1715
w = 10
h = 50

# 创建设备描述表
desktop_dc = win32gui.GetWindowDC(hdesktop)
dc_list = []
bitmap_list = []

for i in range(10):
    time.sleep(1)
    # 创建一个内存设备描述表
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)
    mem_dc = img_dc.CreateCompatibleDC()

    bitmap = win32ui.CreateBitmap()
    # 创建位图对象
    bitmap.CreateCompatibleBitmap(img_dc, w, h)
    mem_dc.SelectObject(bitmap)

    # 截图至内存设备描述表
    mem_dc.BitBlt((0, 0), (w, h), img_dc, (left, top), win32con.SRCCOPY)
    dc_list.append(mem_dc)
    bitmap_list.append(bitmap)

for i, (dc, bitmap) in enumerate(zip(dc_list, bitmap_list)):
    bitmap.SaveBitmapFile(dc, 'screens/' + str(i) + '.png')
    dc.DeleteDC()
    win32gui.DeleteObject(bitmap.GetHandle())