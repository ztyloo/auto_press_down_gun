

all_guns = ['98k', 'akm', 'aug', 'awm', 'dp28', 'groza', 'm16', 'm24', 'm249', 'm416', 'm762', 'mini14', 'mk14',
                 'mk47', 'qbu', 'qbz', 's12k', 's1987', 's686', 'scar', 'sks', 'slr', 'tommy', 'ump9', 'uzi', 'vector',
                 'vss', 'win94', 'pp19', 'g36c']

single_guns = ['98k', 'awm', 'm16', 'm24', 'mini14', 's12k', 's1987', 's686', 'sks', 'slr', 'win94']
full_guns = ['dp28', 'm249']
single_burst_guns = ['m16', ]
single_full_guns = ['akm', 'aug', 'groza', 'm416', 'qbz', 'scar', 'mk14', 'tommy', 'uzi', 'vss']
single_burst_full_guns = ['m762', 'ump45', 'vector']
can_full_guns = ['akm', 'aug', 'groza', 'm416', 'qbz', 'scar', 'mk14', 'tommy', 'uzi', 'vss', 'm762', 'ump45', 'vector', 'dp28', 'm249', 'pp19', 'g36c']


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

    def set_fire_mode(self, fire_mode):
        if self.name in can_full_guns:
            if fire_mode != '':
                self.fire_mode = fire_mode

    def set_name(self, name):
        if name != '':
            self.name = name

    def set_scope(self, scope):
        if scope != '':
            self.scope = scope

    def set_muzzle(self, muzzle):
        if muzzle != '':
            self.muzzle = muzzle

    def set_grip(self, grip):
        if grip != '':
            self.grip = grip


class All_States():
    def __init__(self):
        self.in_tab = False
        self.in_scope = False

        self.weapon_n = 0
        self.weapon = [Weapon(), Weapon()]

        self.hm = None
        self.bp = None
        self.vt = None


if __name__ == '__main__':
    states = All_States()
