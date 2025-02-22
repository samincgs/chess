from .piece import Piece

class Horse(Piece):
    def __init__(self, board, color, pos):
        super().__init__(board, color, pos)
        self.type =  'horse'
        self.load_piece()