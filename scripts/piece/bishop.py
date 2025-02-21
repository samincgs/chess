from .piece import Piece

class Bishop(Piece):
    def __init__(self, board, color):
        super().__init__(board, color)
        self.type =  'bishop'
        self.load_piece()
        