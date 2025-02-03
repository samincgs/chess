from .piece import Piece

class King(Piece):
    def __init__(self, pos, color):
        self.type = 'king'
        super().__init__(pos, color)