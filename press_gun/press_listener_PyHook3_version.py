import threading
import pythoncom
import PyHook3 as pyHook
from press_gun.press import Press


class Press_Listener(threading.Thread):
    def __init__(self, all_states):
        threading.Thread.__init__(self)
        self.all_states = all_states
        self.press = Press(self.all_states)

        self._loop = True

    def _hook_on_mouse(self, event):
        # print('---------------------------------------------')
        # print("MessageName:", event.MessageName)
        # print("Message:", event.Message)
        # print("Time:", event.Time)
        # print("Window:", event.Window)
        # print("WindowName:", event.WindowName)
        # print("Injected:", event.Injected)

        if event.Message == 513:  # mouse left down
            print('press.start')
            self.press.start()
        if event.Message == 514:  # mouse left up
            print('press.stop')
            self.press.stop()
            self.press = Press(self.all_states)
            print('after Press')

        return True

    def run(self):
        print('run')
        self.hm = pyHook.HookManager()
        self.hm.MouseAllButtons = self._hook_on_mouse
        self.hm.HookMouse()
        while self._loop:
            pythoncom.PumpWaitingMessages()  # 只有第一次能正常工作

    def stop(self):
        self._loop = False


if __name__ == '__main__':
    from all_states import All_States

    all_states = All_States()
    all_states.weapon[0].name = 'scar'
    all_states.weapon[0].scope = '1'

    pl = Press_Listener(all_states)
    pl.run()
