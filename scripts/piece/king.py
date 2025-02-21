from .piece import Piece

class King(Piece):
    def __init__(self, board, color):
        super().__init__(board, color)
        self.type =  'king'
        self.load_piece()