from .piece import Piece

class Queen(Piece):
    def __init__(self, board, pos, color):
        self.type = 'queen'
        super().__init__(board, pos, color)