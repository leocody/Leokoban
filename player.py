import pyxel
from constant import PYSIZE, HALFPYSIZE, SCREEN_HEIGHT, SCREEN_WIDTH

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.step = 0

    #Move Logic

    def move_up(self):
        self.y -= 1
        self.step += 1

    def move_down(self):
        self.y += 1
        self.step += 1

    def move_left(self):
        self.x -= 1
        self.step += 1

    def move_right(self):
        self.x += 1
        self.step += 1

    #Push Logic

    def push_and_move_up(self, box):
        box.move_up()
        self.move_up()

    def push_and_move_down(self, box):
        box.move_down()
        self.move_down()


    def push_and_move_left(self, box):
        box.move_left()
        self.move_left()

    def push_and_move_right(self, box):
        box.move_right()
        self.move_right()
        

    #DRAW LOGIC
    def draw(self):
        pyxel.blt(self.x * PYSIZE, self.y * PYSIZE, 0, 16, 0, 16, 16)
        pyxel.text(1, SCREEN_HEIGHT - 9, "Walk Step : " + str(self.step), pyxel.COLOR_WHITE)


