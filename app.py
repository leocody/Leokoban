import pyxel

COURSE_LAYOUT = [
    [2, 2, 2, 2, 2],
    [2, 0, 0, 0, 2],
    [2, 1, 3, 0, 2],
    [2, 0, 0, 4, 2],
    [2, 2, 2, 2, 2]
]

PYSIZE = 8 * 2
HALFPYSIZE = PYSIZE / 2
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
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, caption="Leokoban")
        pyxel.load("assets/images.pyxres")
        pyxel.run(self.draw, self.update)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q) or pyxel.btnp(pyxel.GAMEPAD_1_A):
            pyxel.quit()
    
    def draw(self):
        for y, line in enumerate(self.course):
            for x, square in enumerate(line):
                if square == EMPTY:
                    pass
                    # pyxel.blt(x * PYSIZE, y * PYSIZE, 0, 0, 0, 16, 16)
                elif square == PLAYER:
                    pyxel.blt(x * PYSIZE, y * PYSIZE, 0, 16, 0, 16, 16)
                elif square == WALL:
                    pyxel.blt(x * PYSIZE, y * PYSIZE, 0, 32, 0, 16, 16)
                elif square == BOX:
                    pyxel.blt(x * PYSIZE, y * PYSIZE, 0, 48, 0, 16, 16)
                elif square == GOAL:
                    pyxel.blt(x * PYSIZE, y * PYSIZE, 0, 0, 16, 16, 16)
                else:
                    print("Unknown")


App(COURSE_LAYOUT)
