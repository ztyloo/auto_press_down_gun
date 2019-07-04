import threading
from pynput import mouse
from pynput.mouse import Button


class Mouse_Press_Listener(mouse.Listener):
    def __init__(self, all_states):
        mouse.Listener.__init__(self)

    def on_click(self, x, y, button, pressed):
        if button == Button.left and pressed:
            self.press = Press(self.dist_seq, self.time_seq)
            self.press.start()
        if button == Button.left and not pressed:
            self.press.stop()
            self.build_new = True
        if not pressed:
            return False

    def

    def get(self):
        return mouse.Listener(on_click=self.on_click, suppress=False)


if __name__ == '__main__':
    import time
    from all_states import All_States

    all_states = All_States()
    all_states.weapon[0].fire_mode = 'full'
    all_states.weapon[0].name = 'scar'
    all_states.weapon[0].scope = '1'

    pl = Mouse_Press_Listener(all_states)
    pl.start()
    time.sleep(60)
    pl.stop()
