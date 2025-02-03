from .piece import Piece

class Bishop(Piece):
    def __init__(self, pos, color):
        self.type = 'bishop'
        super().__init__(pos, color)