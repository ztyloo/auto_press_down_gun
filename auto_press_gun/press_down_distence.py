
class Down_distence:
    def __init__(self, k, b, tms):
        self.b = b
        self.k = k
        self.x = 0
        self.tms = tms

    def pop(self):
        if self.x == 0:
            y = 2*self.b
        else:
            y = self.k * self.x + self.b
        self.x += 1
        return y*self.tms
