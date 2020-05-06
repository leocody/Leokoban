import pyxel
from player import Player
from box import Box
from constant import PYSIZE, HALFPYSIZE

COURSE_LAYOUT = [
    [2, 2, 2, 2, 2],
    [2, 0, 0, 0, 2],
    [2, 0, 0, 0, 2],
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
        self.box = Box(2, 2)
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, caption="Leokoban")
        pyxel.load("assets/images.pyxres")
        pyxel.run(self.draw, self.update)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q) or pyxel.btnp(pyxel.GAMEPAD_1_A):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD_1_UP):
            nextposition = self.course[self.player.y - 1][self.player.x]
            if nextposition != WALL:
                self.player.move_up()   
        
        if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD_1_DOWN):
            nextposition = self.course[self.player.y + 1][self.player.x]
            if nextposition != WALL:
                self.player.move_down()    
        
        if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.GAMEPAD_1_LEFT):
            nextposition = self.course[self.player.y][self.player.x - 1]
            if nextposition != WALL:
                self.player.move_left()   
        
        if pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.GAMEPAD_1_RIGHT):
            nextposition = self.course[self.player.y][self.player.x + 1]
            if nextposition != WALL:
                self.player.move_right()   
        

    #DRAW LOGIC   
    def draw(self):
        pyxel.cls(pyxel.COLOR_BLACK)
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
                    pass
                elif square == GOAL:
                    pyxel.blt(x * PYSIZE, y * PYSIZE, 0, 0, 16, 16, 16)
                else:
                    print("Unknown")
        self.player.draw()
        self.box.draw()


App(COURSE_LAYOUT)
