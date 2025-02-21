from .piece import Piece

class Rook(Piece):
    def __init__(self, board, color):
        super().__init__(board, color)
        self.type = 'rook'
        self.load_piece()
        
        
    