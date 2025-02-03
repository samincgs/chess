from .piece import Piece

class Queen(Piece):
    def __init__(self, pos, color):
        self.type = 'queen'
        super().__init__(pos, color)