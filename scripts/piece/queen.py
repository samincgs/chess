from .piece import Piece

class Queen(Piece):
    def __init__(self, board, color):
        super().__init__(board, color)
        self.type =  'queen'
        self.load_piece()