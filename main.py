from listeners import Key_Listener


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
    k = Key_Listener(states)
    k.run()
