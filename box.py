import pyxel
from constant import PYSIZE, HALFPYSIZE, WALL, U_to_D, D_to_U, L_to_R, R_to_L

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

    def is_collision(self, player_nxt_pos_x, player_nxt_pos_y):
        if player_nxt_pos_x == self.x and player_nxt_pos_y == self.y:
            return True
        else:
            return False

    def can_move(self, stage, other_boxes, direction):
        if self.no_wall(stage, direction) and self.no_boxes(other_boxes, direction):
            return True
        return False

    def no_wall(self, stage, direction):
        if direction == D_to_U:   
            kind = stage.get_kind(self.x, self.y - 1)

        if direction == U_to_D:
            kind = stage.get_kind(self.x, self.y + 1)

        if direction == L_to_R:
            kind = stage.get_kind(self.x + 1, self.y)

        if direction == R_to_L:
            kind = stage.get_kind(self.x - 1, self.y)

        if kind == WALL:
            return False
        return True

    def no_boxes(self, other_boxes, direction):

        if direction == L_to_R:
            for other_box in other_boxes:
                if self.x + 1 == other_box.x and self.y == other_box.y:
                    return False
        
        if direction == R_to_L:
            for other_box in other_boxes:
                if self.x - 1 == other_box.x and self.y == other_box.y:
                    return False

        if direction == U_to_D:
            for other_box in other_boxes:
                if self.x == other_box.x and self.y + 1 == other_box.y:
                    return False
        
        if direction == D_to_U:
            for other_box in other_boxes:
                if self.x == other_box.x and self.y - 1 == other_box.y:
                    return False

        return True




