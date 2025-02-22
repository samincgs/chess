from .piece import Piece

class Bishop(Piece):
    def __init__(self, board, color, pos):
        super().__init__(board, color, pos)
        self.type =  'bishop'
        self.load_piece()
        