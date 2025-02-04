from .piece import Piece

class King(Piece):
    def __init__(self, board, pos, color):
        self.type = 'king'
        super().__init__(board, pos, color)