
class Down_distence:
    def __init__(self, dis_list, tms):
        self.tms = tms
        self.x = 0
        self.dis_list = dis_list
        self.lenth = len(self.dis_list)

    def pop(self):
        if self.x < self.lenth:
            y = self.dis_list[self.x]
            self.x += 1
        else:
            y = 0
        return y*self.tms

    def reset(self):
        self.x = 0


