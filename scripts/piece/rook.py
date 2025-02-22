from .piece import Piece

class Rook(Piece):
    def __init__(self, board, color, pos):
        super().__init__(board, color, pos)
        self.type = 'rook'
        self.load_piece()
        
        
    