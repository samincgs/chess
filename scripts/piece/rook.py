from .piece import Piece

class Rook(Piece):
    def __init__(self, board, pos, color):
        self.type = 'rook'
        super().__init__(board, pos, color)