import pyxel

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Move Logic

    def move_up(self):
        pass

    def move_down(self):
        pass

    def move_left(self):
        pass

    def move_right(self):
        pass

    #Push Logic

    def push_up(self, box):
        self.move_up()
        box.box_move_up()
        pass

    def push_down(self, box):
        pass

    def push_left(self, box):
        pass

    def push_right(self, box):
        pass

