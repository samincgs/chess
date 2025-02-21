from .piece import Piece

class Pawn(Piece):
    def __init__(self, board, color):
        super().__init__(board, color)
        self.type =  'pawn'
        self.load_piece()