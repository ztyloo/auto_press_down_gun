
class Down_distence:
    def __init__(self, k, b, tms):
        self.b = b
        self.k = k
        self.x = 0
        self.tms = tms

        self.i = 0
        self.list = [42, 18, -24, -4]

    def pop(self):
        if self.i < 4:
            y = self.list[self.i]
            self.i += 1
        else:
            y = 0
        print(y)
        return y*self.tms

    def reset(self):
        self.i = 0
