from .piece import Piece

class Bishop(Piece):
    def __init__(self, board, pos, color):
        self.type = 'bishop'
        super().__init__(board, pos, color)