import pyxel
from player import Player
from constant import PYSIZE, HALFPYSIZE

COURSE_LAYOUT = [
    [2, 2, 2, 2, 2],
    [2, 0, 0, 0, 2],
    [2, 0, 3, 0, 2],
    [2, 0, 0, 4, 2],
    [2, 2, 2, 2, 2]
]

SCREEN_WIDTH = 5 * PYSIZE
SCREEN_HEIGHT = 5 * PYSIZE
EMPTY = 0
PLAYER = 1
WALL = 2
BOX = 3
GOAL = 4
class App:
    def __init__(self, course):
        self.course = course
        self.player = Player(1, 2)
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, caption="Leokoban")
        pyxel.load("assets/images.pyxres")
        pyxel.run(self.draw, self.update)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q) or pyxel.btnp(pyxel.GAMEPAD_1_A):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD_1_UP):
            self.player.move_up()

            

    #DRAW LOGIC   
    def draw(self):
        for y, line in enumerate(self.course):
            for x, square in enumerate(line):
                if square == EMPTY:
                    pass
                    # pyxel.blt(x * PYSIZE, y * PYSIZE, 0, 0, 0, 16, 16)
                elif square == PLAYER:
                    pass
                    #pyxel.blt(x * PYSIZE, y * PYSIZE, 0, 16, 0, 16, 16)
                elif square == WALL:
                    pyxel.blt(x * PYSIZE, y * PYSIZE, 0, 32, 0, 16, 16)
                elif square == BOX:
                    pyxel.blt(x * PYSIZE, y * PYSIZE, 0, 48, 0, 16, 16)
                elif square == GOAL:
                    pyxel.blt(x * PYSIZE, y * PYSIZE, 0, 0, 16, 16, 16)
                else:
                    print("Unknown")
        self.player.draw()


App(COURSE_LAYOUT)
