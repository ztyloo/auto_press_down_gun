import threading
import tkinter, win32api, win32con, pywintypes


# screen_width = win32api.GetSystemMetrics(0)
# screen_height = win32api.GetSystemMetrics(1)


class Show_Watermark(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._loop = True

        self.tk = tkinter.Tk()
        self.tk.overrideredirect(True)  # 隐藏显示框
        self.tk.lift()  # 置顶层
        self.tk.wm_attributes("-topmost", True)  # 始终置顶层
        self.tk.wm_attributes("-disabled", True)
        self.tk.wm_attributes("-transparentcolor", "white")  # 白色背景透明
        hWindow = pywintypes.HANDLE(int(self.tk.frame(), 16))
        exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
        win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

    def set_text(self, text, xy, size):
        self.tk.geometry("+"+str(xy[0])+"+"+str(xy[1])+"")  # 设置窗口位置或大小
        label = tkinter.Label(text=text, compound='left', font=('Times New Roman', str(size)), fg='#d5d5d5', bg='white')
        label.pack()  # 显示

    def run(self):
        while self._loop:
            self.tk.update_idletasks()
            self.tk.update()

    def stop(self):
        self._loop = False


if __name__ == '__main__':
    show = Show_Watermark()
    show.set_text('t t t t', (2500, 500), 20)
    show.run()


