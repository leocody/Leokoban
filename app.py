import pyxel
from player import Player
from box import Box
from constant import PYSIZE, HALFPYSIZE, SCREEN_HEIGHT, SCREEN_WIDTH, GOAL, WALL, U_to_D, D_to_U, L_to_R, R_to_L
from stages import Stage1



class App:
    def __init__(self, stage):
        self.stage = stage
        self.reset()
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, caption="Leokoban")
        pyxel.load("assets/images.pyxres")
        pyxel.run(self.draw, self.update)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q) or pyxel.btnp(pyxel.GAMEPAD_1_A):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_R) or pyxel.btnp(pyxel.GAMEPAD_1_B):
            self.reset()

        if self.gameover or self.goal: return 

        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD_1_UP):
            self.handle_up_key()
        
        if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD_1_DOWN):
            self.handle_down_key()
        
        if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.GAMEPAD_1_LEFT):
            self.handle_left_key()
        
        if pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.GAMEPAD_1_RIGHT):
            self.handle_right_key()

            
        self.check_complete()
        self.check_gameover()

    def check_complete(self):
        box_pos1 = self.stage.get_kind(self.box.x, self.box.y)
        box_pos2 = self.stage.get_kind(self.box2.x, self.box2.y)
        box_pos3 = self.stage.get_kind(self.box3.x, self.box3.y)
        if box_pos1 == GOAL and box_pos2 == GOAL and box_pos3 == GOAL:
            self.goal = True

    def check_gameover(self):
        if self.player.step >= self.stage.limit:
            self.gameover = True

    def handle_up_key(self):
        if self.box.is_collision(self.player.x, self.player.y - 1):
            if self.box.can_move(self.stage, [self.box2, self.box3], D_to_U):
                self.player.push_and_move_up(self.box)

        elif self.box2.is_collision(self.player.x, self.player.y - 1):
            if self.box2.can_move(self.stage, [self.box, self.box3], D_to_U):
                self.player.push_and_move_up(self.box2)
        
        elif self.box3.is_collision(self.player.x, self.player.y - 1):
            if self.box3.can_move(self.stage, [self.box, self.box2], D_to_U):
                self.player.push_and_move_up(self.box3)
        else:
            nextposition = self.stage.layout[self.player.y - 1][self.player.x]
            if nextposition != WALL:
                self.player.move_up()

    def handle_down_key(self):
        if self.box.is_collision(self.player.x ,self.player.y + 1):
            if self.box.can_move(self.stage, [self.box2, self.box3], U_to_D):
                self.player.push_and_move_down(self.box)

        elif self.box2.is_collision(self.player.x ,self.player.y + 1):
            if self.box2.can_move(self.stage, [self.box, self.box3], U_to_D):
                self.player.push_and_move_down(self.box2)        

        elif self.box3.is_collision(self.player.x ,self.player.y + 1):
            if self.box3.can_move(self.stage, [self.box, self.box2], U_to_D):
                self.player.push_and_move_down(self.box3)     

        else:
            nextposition = self.stage.layout[self.player.y + 1][self.player.x]
            if nextposition != WALL:
                self.player.move_down()  

    def handle_left_key(self):
        if self.box.is_collision(self.player.x - 1, self.player.y):
            if self.box.can_move(self.stage, [self.box2, self.box3], R_to_L):
                self.player.push_and_move_left(self.box)

        elif self.box2.is_collision(self.player.x - 1, self.player.y):
            if self.box2.can_move(self.stage, [self.box, self.box3], R_to_L):
                self.player.push_and_move_left(self.box2)

        elif self.box3.is_collision(self.player.x - 1, self.player.y):
            if self.box3.can_move(self.stage, [self.box, self.box2], R_to_L):
                self.player.push_and_move_left(self.box3)

        else:
            nextposition = self.stage.layout[self.player.y][self.player.x - 1]
            if nextposition != WALL:
                self.player.move_left()   

    def handle_right_key(self):
        if self.box.is_collision(self.player.x + 1, self.player.y):
            if self.box.can_move(self.stage, [self.box2, self.box3], L_to_R):
                self.player.push_and_move_right(self.box)

        elif self.box2.is_collision(self.player.x + 1, self.player.y):
            if self.box2.can_move(self.stage, [self.box, self.box3], L_to_R):
                self.player.push_and_move_right(self.box2)
        elif self.box3.is_collision(self.player.x + 1, self.player.y):
            if self.box3.can_move(self.stage, [self.box, self.box2], L_to_R):
                self.player.push_and_move_right(self.box3)

        else:
            nextposition = self.stage.layout[self.player.y][self.player.x + 1]
            if nextposition != WALL:
                self.player.move_right() 

    
        #RESET LOGIC
    def reset(self):
        self.player = Player(self.stage.playerx, self.stage.playery)
        self.box = Box(self.stage.boxx, self.stage.boxy)
        self.box2 = Box(self.stage.box2_x, self.stage.box2_y)
        self.box3 = Box(self.stage.box3_x, self.stage.box3_y)
        self.goal = False
        self.gameover = False



    #DRAW LOGIC  
    def draw(self):
        pyxel.cls(pyxel.COLOR_BLACK)
        self.stage.draw()
        self.player.draw()
        self.box.draw()
        self.box2.draw()
        self.box3.draw()

        if self.goal:            #CHECK IF IT IS GOAL
            pyxel.text(
                SCREEN_WIDTH / 2 - 35, 
                SCREEN_HEIGHT / 2,
                "GOAL! YOU MADE IT!",
                11)
        elif self.gameover:         #CHECK IF IT IS GAMEOVER
            pyxel.text(SCREEN_HEIGHT / 2 - 35,
             SCREEN_HEIGHT / 2, 
             "GAME OVER!!", 
             pyxel.COLOR_RED) 



App(Stage1())
