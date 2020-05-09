
from constant import GOAL, WALL, EMPTY, PYSIZE
import pyxel

class Stage1:
    def __init__(self):
        # self.layout = [
        #     [2, 2, 2, 2, 2, 2, 2, 2, 0],
        #     [2, 0, 0, 0, 4, 4, 4, 0, 2],
        #     [2, 0, 0, 0, 0, 0, 0, 0, 2],
        #     [2, 0, 0, 0, 0, 0, 0, 0, 2],
        #     [2, 0, 0, 0, 0, 0, 0, 0, 2],
        #     [2, 0, 0, 0, 0, 0, 0, 0, 2],
        #     [2, 0, 0, 0, 0, 0, 0, 0, 2],
        #     [2, 2, 2, 2, 2, 2, 2, 2, 2]
        # ]
        self.layout = [
            [0, 2, 2, 2, 2, 2, 2, 2, 0],
            [0, 2, 0, 0, 4, 4, 4, 2, 0],
            [0, 2, 0, 0, 0, 2, 2, 2, 2],
            [0, 2, 2, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 2, 0, 2, 0, 2],
            [2, 0, 0, 0, 2, 0, 0, 0, 2],
            [2, 0, 0, 0, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 0, 0, 0, 0]
        ]
        self.playerx = 3
        self.playery = 1
        self.boxx = 2
        self.boxy = 5
        self.box2_x = 3
        self.box2_y = 3
        self.box3_x = 5
        self.box3_y = 4
        self.limit = 80


    def draw(self):
        for y, line in enumerate(self.layout):
            for x, square in enumerate(line):
                if square == WALL:
                    pyxel.blt(x * PYSIZE, y * PYSIZE, 0, 32, 0, 16, 16)
                elif square == GOAL:
                    pyxel.blt(x * PYSIZE, y * PYSIZE, 0, 0, 16, 16, 16)
    
    def get_kind(self, x, y):
        return self.layout[y][x]


if __name__ == "__main__":
    st = Stage1()
    assert st.get_kind(0, 0) == EMPTY
    assert st.get_kind(0, 4) == WALL
    assert st.get_kind(5, 1) == GOAL
