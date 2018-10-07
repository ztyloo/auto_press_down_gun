

class State:
    def __init__(self):
        self.gun_state = 1
        self.fire_mode1 = None

        self.gun0 = None  # gun in use
        self.scope0 = 1

        self.gun1 = None
        self.scope1 = 1

        self.gun2 = None
        self.scope2 = 1

        self.hm = None
        self.bp = None
        self.vt = None

    def update(self):
        self.update_gun()

    def update_gun(self):
        if self.gun_state == 1:
            self.gun0 = self.gun1
            self.scope0 = self.scope1
        elif self.gun_state == 2:
            self.gun0 = self.gun2
            self.scope0 = self.scope2




