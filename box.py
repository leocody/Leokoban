import pyxel
from constant import PYSIZE, HALFPYSIZE

class Box:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Move Logic

    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1
    
    #DRAW LOGIC
    def draw(self):
        pyxel.blt(self.x * PYSIZE, self.y * PYSIZE, 0, 48, 0, 16, 16)




