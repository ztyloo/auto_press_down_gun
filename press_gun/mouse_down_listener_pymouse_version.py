from pymouse import PyMouseEvent


class Mouse_Press_Listener(PyMouseEvent):
    def __init__(self, left_pressing_flag):
        PyMouseEvent.__init__(self)
        self.left_pressing_flag = left_pressing_flag

    def click(self, x, y, button, press):
        if button == 1 and press:
            self.left_pressing_flag = True
        if button == 1 and not press:
            self.left_pressing_flag = False
        if not button:
            return False


if __name__ == '__main__':
    from all_states import All_States

    all_states = All_States()
    all_states.weapon[0].name = 'scar'
    all_states.weapon[0].scope = '1'

    pl = Mouse_Press_Listener(all_states)
    pl.run()
