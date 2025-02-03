from .piece import Piece

class Rook(Piece):
    def __init__(self, pos, color):
        self.type = 'rook'
        super().__init__(pos, color)