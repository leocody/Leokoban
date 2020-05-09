import pyxel
from player import Player
from box import Box
from constant import PYSIZE, HALFPYSIZE, SCREEN_HEIGHT, SCREEN_WIDTH, GOAL, WALL, U_to_D, D_to_U, L_to_R, R_to_L
from stages import Stage1, Stage2, Stage3



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

        for box in self.boxes:
            if self.stage.get_kind(box.x, box.y) == GOAL:
                self.goal = True
                continue
                
            else:
                self.goal = False
                break

    def check_gameover(self):
        if self.player.step >= self.stage.limit:
            self.gameover = True


    def handle_up_key(self):
        if not self.player.can_move(self.stage, D_to_U):
            return

        for box in self.boxes:
            if box.is_collision(self.player.x, self.player.y - 1):
                if box.can_move(self.stage, self.boxes, D_to_U):
                    self.player.push_and_move_up(box)

                return

        self.player.move_up()




    def handle_down_key(self):
        if not self.player.can_move(self.stage, U_to_D):
            return

        for box in self.boxes:
            if box.is_collision(self.player.x, self.player.y + 1):
                if box.can_move(self.stage, self.boxes, U_to_D):
                    self.player.push_and_move_down(box)

                return

        self.player.move_down()

    def handle_left_key(self):
        if not self.player.can_move(self.stage, R_to_L):
            return

        for box in self.boxes:
            if box.is_collision(self.player.x - 1, self.player.y):
                if box.can_move(self.stage, self.boxes, R_to_L):
                    self.player.push_and_move_left(box)

                return

        self.player.move_left()

    def handle_right_key(self):
        if not self.player.can_move(self.stage, L_to_R):
            return

        for box in self.boxes:
            if box.is_collision(self.player.x + 1, self.player.y):
                if box.can_move(self.stage, self.boxes, L_to_R):
                    self.player.push_and_move_right(box)

                return

        self.player.move_right()

    
        #RESET LOGIC
    def reset(self):
        self.player = Player(self.stage.player[0], self.stage.player[1])
        self.boxes = []
        self.goal = False
        self.gameover = False
        for i in range(self.stage.box_count):
            box_tuple = self.stage.boxes[i]
            box = Box(box_tuple[0], box_tuple[1])
            self.boxes.append(box)




    #DRAW LOGIC  
    def draw(self):
        pyxel.cls(pyxel.COLOR_BLACK)
        self.stage.draw()
        self.player.draw()
        for box in self.boxes:
            box.draw()

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



App(Stage3())
