
class Down_distence:
    def __init__(self, tms):
        self.tms = tms
        self.x = 0
        self.ak_dis_list = [87, 30, 60, 70, 80, 60, 80, 65, 70, 60, 80]
        self.mk47_dis_list_6times = [142, 78, 98, 131, 154, 152, 151, 151, 165]
        self.dis_list = self.mk47_dis_list_6times
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


