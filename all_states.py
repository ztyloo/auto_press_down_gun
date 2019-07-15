
from press_gun.time_periods_constant import time_periods
from press_gun.generate_distance.gun_distance_constant import dist_lists


all_guns = ['98k', 'akm', 'aug', 'awm', 'dp28', 'groza', 'm16', 'm24', 'm249', 'm416', 'm762', 'mini14', 'mk14',
                 'mk47', 'qbu', 'qbz', 's12k', 's1987', 's686', 'scar', 'sks', 'slr', 'tommy', 'ump9', 'uzi', 'vector',
                 'vss', 'win94', 'pp19', 'g36c']

single_guns = ['98k', 'awm', 'm16', 'm24', 'mini14', 's12k', 's1987', 's686', 'sks', 'slr', 'win94']
full_guns = ['dp28', 'm249']
single_burst_guns = ['m16', ]
single_full_guns = ['akm', 'aug', 'groza', 'm416', 'qbz', 'scar', 'mk14', 'tommy', 'uzi', 'vss']
single_burst_full_guns = ['m762', 'ump45', 'vector']
can_full_guns = ['akm', 'aug', 'groza', 'm416', 'qbz', 'scar', 'mk14', 'tommy', 'uzi', 'vss', 'm762', 'ump45', 'vector', 'dp28', 'm249', 'pp19', 'g36c']

ARs = ['akm', 'aug', 'groza', 'm416', 'qbz', 'scar', 'm762', 'pp19', 'g36c']
SMGs = ['tommy', 'uzi', 'ump45', 'vector', 'pp19', 'g36c']
SPs = ['98k','m24', 'mini14', 'mk14', 'qbz', 'sks', 'slr', 'vss']


def factor_scope(scope):
    factor = 1
    if scope == 1:
        factor = 1.5
    if scope == 2:
        factor = 1.
    if scope == 3:
        factor = 1.
    if scope == 4:
        factor = 1.1
    if scope == 6:
        factor = 0.8
    return scope * factor


def calculate_press_seq(name, scope_factor):
    scope_factor = factor_scope(scope_factor)
    dist_interval = dist_lists.get(name, [])
    dist_interval = [i * scope_factor for i in dist_interval]
    time_interval = time_periods.get(name, 1)
    divide_num = int(time_interval/0.02)  # 整数分割

    time_sequence = list()
    dist_sequence = list()
    for dist in dist_interval:
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
        self.butt = ''

        self.all_factor = 1
        self.scope_factor = 1
        self.muzzle_factor = 1
        self.grip_factor = 1
        self.butt_factor = 1

        self.dist_seq = list()
        self.time_seq = list()

    def set_fire_mode(self, fire_mode):
        if fire_mode == '' or self.fire_mode == fire_mode:
            return False
        self.fire_mode = fire_mode
        return True

    def set_name(self, name):
        if name == '' or self.name == name:
            return False
        self.name = name
        return True

    def set_scope(self, scope):
        if scope == '' or self.scope == scope:
            return False
        self.scope = scope
        self.scope_factor = int(scope.replace('r', '').replace('h', ''))
        if self.name == 'vss':
            self.scope_factor = 4
        return True

    def set_muzzle(self, muzzle):
        if muzzle == '' or self.muzzle == muzzle:
            return False
        self.muzzle = muzzle
        if self.muzzle == 'flash':
            self.muzzle_factor = 0.9

        elif self.muzzle == 'suppressor':  # 消音
            self.muzzle_factor = 1.0

        elif self.muzzle == 'compensator':
            if self.name in ARs:
                self.muzzle_factor = 0.85
            elif self.name in SMGs:
                self.muzzle_factor = 0.75
            elif self.name in SPs:
                self.muzzle_factor = 0.8
        return True

    def set_grip(self, grip):
        if grip == '' or self.grip == grip:
            return False
        self.grip = grip
        if self.grip == 'thumb':
            self.grip_factor = 0.85
        elif self.grip == 'lightweight':
            self.grip_factor = 1.25
        elif self.grip == 'half':
            self.grip_factor = 0.9
        elif self.grip == 'Angled':
            self.grip_factor = 1.0
        elif self.grip == 'vertical':
            self.grip_factor = 0.85
        return True

    def set_butt(self, butt):
        if butt == '' or self.butt == butt:
            return False
        if self.name == 'm416' and butt == 'm416_butt':
            self.butt_factor = 0.85
        self.butt = butt
        return True

    def set_seq(self):
        self.all_factor = self.scope_factor * self.muzzle_factor * self.grip_factor * self.butt_factor
        self.dist_seq, self.time_seq = calculate_press_seq(self.name, self.all_factor)


class All_States():
    def __init__(self):
        self.dont_press = False
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
