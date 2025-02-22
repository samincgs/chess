from .piece import Piece

class King(Piece):
    def __init__(self, board, color, pos):
        super().__init__(board, color, pos)
        self.type =  'king'
        self.load_piece()