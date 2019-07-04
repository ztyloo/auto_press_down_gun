import threading
from pynput import mouse
from  pynput.mouse import Button

from press_gun.press import Press


class Press_Listener(threading.Thread):
    def __init__(self, all_states):
        threading.Thread.__init__(self)
        self.all_states = all_states
        n = self.all_states.weapon_n
        if self.all_states.weapon[n].name != '' and self.all_states.weapon[n].fire_mode == 'full':
            self.press = Press(self.all_states)
            self._loop = True
        else:
            self._loop = False

    def on_click(self, x, y, button, pressed):
        if button == Button.left and pressed:
            if not self.press.is_alive():
                self.press = Press(self.all_states)
            self.press.start()
        if button == Button.left and not pressed:
            if self.press.is_alive():
                self.press.stop()
            self.press = Press(self.all_states)
        if not pressed:
            return False

    def run(self):
        while self._loop:
            with mouse.Listener(on_click=self.on_click, suppress = False) as listener:
                listener.join()

    def stop(self):
        self._loop = False


if __name__ == '__main__':
    import time
    from all_states import All_States

    all_states = All_States()
    all_states.weapon[0].fire_mode = 'full'
    all_states.weapon[0].name = 'scar'
    all_states.weapon[0].scope = '1'

    pl = Press_Listener(all_states)
    pl.start()
    time.sleep(60)
    pl.stop()
