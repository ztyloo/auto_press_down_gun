import threading
import pythoncom
import PyHook3 as pyHook
from press_gun.press import Press


class Press_Listener(threading.Thread):
    def __init__(self, all_states):
        threading.Thread.__init__(self)
        self.all_states = all_states
        self.hm = pyHook.HookManager()
        self.hm.MouseAll = self._onMouseEvent
        self._loop = True
        self.press = Press(self.all_states)

    def _onMouseEvent(self, event):
        # print('---------------------------------------------')
        # print("MessageName:", event.MessageName)
        # print("Message:", event.Message)
        # print("Time:", event.Time)
        # print("Window:", event.Window)
        # print("WindowName:", event.WindowName)
        # print("Injected:", event.Injected)

        if event.Message == 513:  # mouse left down
            self.press.start()
        if event.Message == 514:  # mouse left up
            self.press.stop()
            self.press = Press(self.all_states)

        return True

    def run(self):
        self.hm.HookMouse()
        while self._loop:
            pythoncom.PumpWaitingMessages()

    def stop(self):
        self._loop = False


if __name__ == '__main__':
    from main import All_States

    all_states = All_States()
    all_states.weapon[0].name = 'scar'
    all_states.weapon[0].scope = '1'

    pl = Press_Listener(all_states)
    pl.run()
