import threading
from pynput import mouse
from pynput.mouse import Button

from press_gun.press import Press
from press_gun.time_interval_constant import time_intervals
from press_gun.generate_distance.gun_distance_constant import dis_intervals


class Mouse_Press_Listener(threading.Thread):
    def __init__(self, all_states):
        threading.Thread.__init__(self)
        self.mouse_listener = mouse.Listener(on_click=self.on_click, suppress=False)
        self.dist_seq, self.time_seq = calculate_press_seq(all_states)
        self.press = Press(self.dist_seq, self.time_seq)
        self._loop = True
        self.build_new = True

    def on_click(self, x, y, button, pressed):
        if button == Button.left and pressed:
            self.press = Press(self.dist_seq, self.time_seq)
            self.press.start()
        if button == Button.left and not pressed:
            self.press.stop()
            self.build_new = True
        if not pressed:
            return False

    def run(self) -> None:
        while self._loop:
            if self.build_new:
                self.mouse_listener = mouse.Listener(on_click=self.on_click, suppress=False)
                self.mouse_listener.start()
                self.build_new = False

    def stop(self):
        self._loop = False


def factor_scope(scope):
    factor = 1
    if scope == 1:
        factor = 1.1
    if scope == 2:
        factor = 1.
    if scope == 3:
        factor = 1.
    if scope == 4:
        factor = 1.1
    if scope == 6:
        factor = 0.8
    return scope * factor


def calculate_press_seq(all_states):
    gun_n = all_states.weapon_n
    gun_name = all_states.weapon[gun_n].name
    gun_scope = int(all_states.weapon[gun_n].scope.replace('r', '').replace('h', ''))
    gun_scope = factor_scope(gun_scope)
    dis_interval = dis_intervals.get(gun_name, [])
    dis_interval = [i * gun_scope for i in dis_interval]
    time_interval = time_intervals.get(gun_name, 1)
    divide_num = int(time_interval/0.02)  # 整数分割

    time_sequence = list()
    dist_sequence = list()
    for dist in dis_interval:
        for i in range(divide_num):
            time_sequence.append(time_interval/divide_num)
            dist_sequence.append(dist/divide_num)

    return dist_sequence, time_sequence


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
