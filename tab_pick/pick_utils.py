
from pymouse import PyMouse


class Pick(Detection):
    def __init__(self):
        super().__init__()
        self.m = PyMouse()

    def set_drag_position(self, position):
        self.x, self.y = position

    def pick(self):
        self.m.move(self.x, self.y)
        self.m.drag(self.x+1000, self.y)


class Priority_Pick(Pick):
    def __init__(self):
        super().__init__()
        self.priority = []
        self.state = len(self.priority)

    def



