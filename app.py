import pyxel
from player import Player
from box import Box
from constant import PYSIZE, HALFPYSIZE, SCREEN_HEIGHT, SCREEN_WIDTH
COURSE_LAYOUT = [
    [2, 2, 2, 2, 2],
    [2, 0, 0, 0, 2],
    [2, 0, 0, 0, 2],
    [2, 0, 0, 4, 2],
    [2, 2, 2, 2, 2]
]


EMPTY = 0
PLAYER = 1
WALL = 2
BOX = 3
GOAL = 4
class App:
    def __init__(self, course):
        self.course = course
        self.reset()
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, caption="Leokoban")
        pyxel.load("assets/images.pyxres")
        pyxel.run(self.draw, self.update)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q) or pyxel.btnp(pyxel.GAMEPAD_1_A):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD_1_UP):
            if self.box.x == self.player.x and self.box.y == self.player.y - 1:
                box_next_pos = self.course[self.box.y - 1][self.box.x]
                if box_next_pos != WALL:
                    self.player.push_and_move_up(self.box)
            else:
                nextposition = self.course[self.player.y - 1][self.player.x]
                if nextposition != WALL:
                    self.player.move_up()   
        
        if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD_1_DOWN):
            if self.box.x == self.player.x and self.box.y == self.player.y + 1:
                box_next_pos = self.course[self.box.y + 1][self.box.x]
                if box_next_pos != WALL:
                    self.player.push_and_move_down(self.box)
            else:
                nextposition = self.course[self.player.y + 1][self.player.x]
                if nextposition != WALL:
                    self.player.move_down()    
        
        if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.GAMEPAD_1_LEFT):
            if self.box.x == self.player.x - 1 and self.box.y == self.player.y:
                box_next_pos = self.course[self.box.y][self.box.x - 1]
                if box_next_pos != WALL:
                    self.player.push_and_move_left(self.box)
            else:
                nextposition = self.course[self.player.y][self.player.x - 1]
                if nextposition != WALL:
                    self.player.move_left()   
        
        if pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.GAMEPAD_1_RIGHT):
            if self.box.x == self.player.x + 1 and self.box.y == self.player.y:
                box_next_pos = self.course[self.box.y][self.box.x + 1]
                if box_next_pos != WALL:
                    self.player.push_and_move_right(self.box)
            else:
                nextposition = self.course[self.player.y][self.player.x + 1]
                if nextposition != WALL:
                    self.player.move_right() 

        if pyxel.btnp(pyxel.KEY_R) or pyxel.btnp(pyxel.GAMEPAD_1_B):
            self.reset()
            
        self.check_complete()

    def check_complete(self):
        box_pos = self.course[self.box.y][self.box.x]
        if box_pos == GOAL:
            self.goal = True

    #RESET LOGIC
    def reset(self):
        self.player = Player(1, 2)
        self.box = Box(2, 2)
        self.goal = False



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

        #CHECK IF IT IS GOAL

        if self.goal:
            pyxel.text(
                SCREEN_WIDTH / 2 - 35, 
                SCREEN_HEIGHT / 2,
                "GOAL! YOU MADE IT!",
                11)

    


App(COURSE_LAYOUT)
