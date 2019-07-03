

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
