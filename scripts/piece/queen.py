from .piece import Piece

class Queen(Piece):
    def __init__(self, board, color, pos):
        super().__init__(board, color, pos)
        self.type =  'queen'
        self.load_piece()