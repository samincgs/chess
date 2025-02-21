from .piece import Piece

class Horse(Piece):
    def __init__(self, board, color):
        super().__init__(board, color)
        self.type =  'horse'
        self.load_piece()