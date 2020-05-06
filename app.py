import pyxel

COURSE_LAYOUT = [
    [2, 2, 2, 2, 2],
    [2, 0, 0, 0, 2],
    [2, 1, 3, 0, 2],
    [2, 0, 0, 4, 2],
    [2, 2, 2, 2, 2]
]


SCREEN_WIDTH = 5 * 8
SCREEN_HEIGHT = 5 * 8

PLAYER = 1
WALL = 2
BOX = 3
GOAL = 4
class App:
    def __init__(self, course):
        self.course = course
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, caption="Leokoban")
        pyxel.run(self.draw, self.update)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q) or pyxel.btnp(pyxel.GAMEPAD_1_A):
            pyxel.quit()
    
    def draw(self):
        for y, line in enumerate(self.course):
            for x, square in enumerate(line):
                if square == 0:
                    print("Empty")
                elif square == PLAYER:
                    pyxel.circ(x * 8 + 4, y * 8 + 4, 2, pyxel.COLOR_LIME)
                elif square == WALL:
                    pyxel.rect(x * 8, y * 8, 8, 8, pyxel.COLOR_BROWN)
                elif square == BOX:
                    pyxel.rect(x * 8, y * 8, 8, 8, pyxel.COLOR_ORANGE)
                elif square == GOAL:
                    pyxel.circ(x * 8 + 4, y * 8 + 4, 0.5, pyxel.COLOR_CYAN)
                else:
                    print("Unknown")


App(COURSE_LAYOUT)
