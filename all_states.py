
from press_gun.time_interval_constant import time_intervals
from press_gun.generate_distance.gun_distance_constant import dis_intervals


all_guns = ['98k', 'akm', 'aug', 'awm', 'dp28', 'groza', 'm16', 'm24', 'm249', 'm416', 'm762', 'mini14', 'mk14',
                 'mk47', 'qbu', 'qbz', 's12k', 's1987', 's686', 'scar', 'sks', 'slr', 'tommy', 'ump9', 'uzi', 'vector',
                 'vss', 'win94', 'pp19', 'g36c']

single_guns = ['98k', 'awm', 'm16', 'm24', 'mini14', 's12k', 's1987', 's686', 'sks', 'slr', 'win94']
full_guns = ['dp28', 'm249']
single_burst_guns = ['m16', ]
single_full_guns = ['akm', 'aug', 'groza', 'm416', 'qbz', 'scar', 'mk14', 'tommy', 'uzi', 'vss']
single_burst_full_guns = ['m762', 'ump45', 'vector']
can_full_guns = ['akm', 'aug', 'groza', 'm416', 'qbz', 'scar', 'mk14', 'tommy', 'uzi', 'vss', 'm762', 'ump45', 'vector', 'dp28', 'm249', 'pp19', 'g36c']


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


def calculate_press_seq(name, scope):
    scope = int(scope.replace('r', '').replace('h', ''))
    scope = factor_scope(scope)
    dis_interval = dis_intervals.get(name, [])
    dis_interval = [i * scope for i in dis_interval]
    time_interval = time_intervals.get(name, 1)
    divide_num = int(time_interval/0.02)  # 整数分割

    time_sequence = list()
    dist_sequence = list()
    for dist in dis_interval:
        for i in range(divide_num):
            time_sequence.append(time_interval/divide_num)
            dist_sequence.append(dist/divide_num)

    return dist_sequence, time_sequence


def gun_next_mode(gun_name, now_mode):
    if gun_name in single_burst_guns:
        if now_mode == 'single':
            return 'burst'
        if now_mode == 'burst':
            return 'single'

    if gun_name in single_full_guns:
        if now_mode == 'single':
            return 'full'
        if now_mode == 'full':
            return 'single'

    if gun_name in single_burst_full_guns:
        if now_mode == 'single':
            return 'burst'
        if now_mode == 'burst':
            return 'full'
        if now_mode == 'full':
            return 'single'


class Ground():
    pass


class Back():
    pass


class Weapon():
    def __init__(self):
        self.fire_mode = ''
        self.name = ''
        self.scope = '1'
        self.muzzle = ''
        self.grip = ''

        self.dist_seq = list()
        self.time_seq = list()

    def set_fire_mode(self, fire_mode):
        original_fire_mode = self.fire_mode
        if self.name in can_full_guns:
            if fire_mode != '':
                self.fire_mode = fire_mode
        return original_fire_mode != fire_mode

    def set_name(self, name):
        original_name = self.name
        if name != '':
            self.name = name
        is_changed = original_name != name
        if is_changed:
            self.dist_seq, self.time_seq = calculate_press_seq(self.name, self.scope)
        return is_changed

    def set_scope(self, scope):
        original_scope = self.scope
        if scope != '':
            self.scope = scope
        is_changed = original_scope != scope
        if is_changed:
            self.dist_seq, self.time_seq = calculate_press_seq(self.name, self.scope)
        return is_changed

    def set_muzzle(self, muzzle):
        original_muzzle = self.muzzle
        if muzzle != '':
            self.muzzle = muzzle
        return original_muzzle != muzzle

    def set_grip(self, grip):
        original_grip = self.grip
        if grip != '':
            self.grip = grip
        return original_grip != grip


class All_States():
    def __init__(self):
        self.in_tab = False
        self.in_scope = False

        self.weapon_n = 0
        self.weapon = [Weapon(), Weapon()]

        self.hm = None
        self.bp = None
        self.vt = None

    def set_weapon_n(self, weapon_n):
        original_n = self.weapon_n
        self.weapon_n = weapon_n
        return original_n != weapon_n


if __name__ == '__main__':
    states = All_States()
