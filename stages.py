class Stage1:
    def __init__(self):
        self.layout = [
            [0, 2, 2, 2, 2, 2, 2, 2, 0],
            [0, 2, 0, 0, 4, 4, 4, 2, 0],
            [0, 2, 0, 0, 0, 2, 2, 2, 2],
            [2, 2, 2, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 2, 0, 2, 0, 2],
            [2, 0, 0, 0, 2, 0, 0, 0, 2],
            [2, 0, 0, 0, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 0, 0, 0, 0]
        ]
        self.playerx = 3
        self.playery = 1
        self.boxx = 2
        self.boxy = 5
        self.limit = 20
