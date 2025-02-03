from .piece import Piece

class Pawn(Piece):
    def __init__(self, pos, color):
        self.type = 'pawn'
        super().__init__(pos, color)