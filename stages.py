
from constant import GOAL, WALL, EMPTY, PYSIZE, GRASS
import pyxel

class Stage:
    def __init__(self):
        self.layout = []
        self.boxes = []
        self.box_count = 0
        self.player = (0, 0)

    def draw(self):
        for y, line in enumerate(self.layout):
            for x, square in enumerate(line):
                if square == WALL:
                    pyxel.blt(x * PYSIZE, y * PYSIZE, 0, 32, 0, 16, 16)
                elif square == GOAL:
                    pyxel.blt(x * PYSIZE, y * PYSIZE, 0, 0, 16, 16, 16)
                elif square == EMPTY:
                    pyxel.blt(x * PYSIZE, y * PYSIZE, 0, 0, 0, 16, 16)
                elif square == GRASS:
                    pyxel.blt(x * PYSIZE, y * PYSIZE, 0, 16, 16, 16, 16)
    
    def get_kind(self, x, y):
        return self.layout[y][x]

    @staticmethod
    def create_stage(stage_number):

        if stage_number == 0:
            stage = Stage1()

        if stage_number == 1:
            stage = Stage2()

        if stage_number == 2:
            stage = Stage3()

        if stage_number == 3:
            stage = Stage4()
        
        return stage
    
    @staticmethod
    def stage_count_limit():
        return 4

class Stage1(Stage):
    def __init__(self):
        self.layout = [
            [1, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 0, 0, 4, 4, 4, 2, 1],
            [1, 2, 0, 0, 0, 2, 2, 2, 2],
            [1, 2, 2, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 2, 0, 2, 0, 2],
            [2, 0, 0, 0, 2, 0, 0, 0, 2],
            [2, 0, 0, 0, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 1, 1, 1, 1]
        ]
        self.boxes = [
            (2, 5),
            (3, 3),
            (5, 4)
        ]
        self.player = (3, 1)
        self.box_count = 3
        self.limit = 75


class Stage2(Stage):
    def __init__(self):
        self.layout = [
            [2, 2, 2, 2, 2, 1, 1, 1, 1],
            [2, 0, 0, 0, 2, 1, 1, 1, 1],
            [2, 0, 0, 0, 2, 1, 2, 2, 2],
            [2, 0, 0, 0, 2, 1, 2, 4, 2],
            [2, 2, 2, 0, 2, 2, 2, 4, 2],
            [1, 2, 2, 0, 0, 0, 0, 4, 2],
            [1, 2, 0, 0, 0, 2, 0, 0, 2],
            [1, 2, 0, 0, 0, 2, 2, 2, 2],
            [1, 2, 2, 2, 2, 2, 1, 1, 1]
        ]
        self.player = (1, 1)
        self.boxes = [
            (2, 2),
            (2, 3),
            (3, 2)
        ]

        self.box_count = 3
        self.limit = 100

class Stage3(Stage):
    def __init__(self):
        self.layout = [
            [1, 1, 2, 2, 2, 2, 2, 2],
            [1, 1, 2, 0, 0, 0, 0, 2],
            [2, 2, 2, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 4, 4, 0, 2],
            [2, 0, 0, 4, 4, 4, 2, 2],
            [2, 2, 2, 2, 0, 0, 2, 1],
            [1, 1, 1, 2, 2, 2, 2, 1],
        ]
        self.player = (1, 3)
        self.boxes = [
            (2, 4),
            (3, 2),
            (3, 3),
            (4, 2),
            (5, 2)
        ]
        self.box_count = 5
        self.limit = 60


class Stage4(Stage):
    def __init__(self):
        self.layout = [
            [2, 2, 2, 2, 2, 2, 2, 2, 1],
            [2, 0, 0, 0, 0, 0, 0, 2, 1],
            [2, 0, 2, 0, 0, 0, 0, 2, 1],
            [2, 0, 4, 4, 4, 2, 0, 2, 1],
            [2, 2, 4, 4, 4, 0, 0, 2, 2],
            [1, 2, 0, 2, 2, 0, 0, 0, 2],
            [1, 2, 0, 0, 0, 0, 0, 0, 2],
            [1, 2, 0, 0, 2, 0, 0, 0, 2],
            [1, 2, 2, 2, 2, 2, 2, 2, 2]   
        ]
        self.player = (7, 7)
        self.boxes = [
            (2, 6),
            (3, 2),
            (4, 2),
            (5, 4),
            (5, 6),
            (6, 5)
        ]
        self.box_count = 6
        self.limit = 110



