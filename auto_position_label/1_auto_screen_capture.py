import threading
import os
from auto_position_label.crop_position import screen_position_states


class Show_Watermark(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def show(self, ):

        mytext = 'KK 笔记'
        root = tkinter.Tk()
        width = win32api.GetSystemMetrics(0)
        height = win32api.GetSystemMetrics(1)
        root.overrideredirect(True)  # 隐藏显示框
        root.geometry("+0+0")  # 设置窗口位置或大小
        root.lift()  # 置顶层
        root.wm_attributes("-topmost", True)  # 始终置顶层
        root.wm_attributes("-disabled", True)
        root.wm_attributes("-transparentcolor", "white")  # 白色背景透明
        hWindow = pywintypes.HANDLE(int(root.frame(), 16))
        exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
        win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)
        label = tkinter.Label(text=mytext, compound='left', font=('Times New Roman', '15'), fg='#d5d5d5', bg='white')
        label.pack()  # 显示
        root.mainloop()  # 循环

    def run(self):
        while self._loop:
            pass

    def stop(self):
        self._loop = False


def screen_cap(root_path = 'D:/github_project/auto_press_down_gun/auto_position_label/screen_captures'):
    os.makedirs(root_path, exist_ok=True)
    for k, v in screen_position_states.items():
        if len(v) > 0:
            for state in v:
                state_fold = os.path.join(root_path, state)
                os.makedirs(state_fold, exist_ok=True)


# def


if __name__ == '__main__':
    all_from_dir = 'D:/github_project/auto_press_down_gun/auto_position_label/screen_captures/'
    all_to_dir = 'D:/github_project/auto_press_down_gun/image_detect/states_4c_im/'

    # screen_cap()

    import tkinter, win32api, win32con, pywintypes


    mytext = 'KK 笔记'
    root = tkinter.Tk()
    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)
    root.overrideredirect(True)  # 隐藏显示框
    root.geometry("+0+0")  # 设置窗口位置或大小
    root.lift()  # 置顶层
    root.wm_attributes("-topmost", True)  # 始终置顶层
    root.wm_attributes("-disabled", True)
    root.wm_attributes("-transparentcolor", "white")  # 白色背景透明
    hWindow = pywintypes.HANDLE(int(root.frame(), 16))
    exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
    win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)
    label = tkinter.Label(text=mytext, compound='left', font=('Times New Roman', '15'), fg='#d5d5d5', bg='white')
    label.pack()  # 显示
    root.mainloop()  # 循环