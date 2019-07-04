import threading
from pynput import mouse
from pynput.mouse import Button

from press_gun.key_listener import Key_Listener
from press_gun.press import Press


class Actor(threading.Thread):
    def __init__(self, all_states):
        threading.Thread.__init__(self)
        self._loop = True

        self.key_listener = Key_Listener(all_states)

        self.mouse_left_pressing = False
        self.mouse_listener = mouse.Listener(on_click=self.on_click, suppress=False)

    def on_click(self, x, y, button, pressed):
        if button == Button.left and pressed:
            self.mouse_left_pressing = True
        if button == Button.left and not pressed:
            self.mouse_left_pressing = False
        if not pressed:
            return False

    def run(self) -> None:  # TODO
        while self._loop:
            if self.mouse_left_pressing:
                self.


if __name__ == '__main__':
    from all_states import All_States

    all_states = All_States()