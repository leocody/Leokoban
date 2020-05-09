import pyxel
from constant import PYSIZE, HALFPYSIZE, SCREEN_HEIGHT, SCREEN_WIDTH, U_to_D, D_to_U, L_to_R, R_to_L, WALL


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
    
    # If there is wall at the next position of the player, it will return False.
    # In the other hand, if it has no wall at the next position of the player, It will return True.
    def can_move(self, stage, direction):
        if direction == D_to_U:
            stage_square = stage.get_kind(self.x, self.y - 1)
            if stage_square == WALL:
                return False

        if direction == U_to_D:
            stage_square = stage.get_kind(self.x, self.y + 1)
            if stage_square == WALL:
                return False
        
        if direction == L_to_R:
            stage_square = stage.get_kind(self.x + 1, self.y)
            if stage_square == WALL:
                return False
        
        if direction == R_to_L:
            stage_square = stage.get_kind(self.x - 1, self.y)
            if stage_square == WALL:
                return False
        
        return True

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


