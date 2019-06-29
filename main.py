from listeners import Key_Listener, Mouse_listern


class All_States():
    def __init__(self):
        self.in_tab = False
        self.in_scope = False

        self.now_weapon = 1

        self.weapon_1 = None
        self.scope_1 = 1
        self.muzzle_1 = None
        self.grip_1 = None
        self.fire_mode_1 = 'single'

        self.weapon_2 = None
        self.scope_2 = 1
        self.muzzle_2 = None
        self.grip_2 = None
        self.fire_mode_2 = 'single'

        self.hm = None
        self.bp = None
        self.vt = None


if __name__ == '__main__':
    states = All_States()
    k = Key_Listener(states)
    k.run()
    # m = Mouse_listern(states)
    # m.run()