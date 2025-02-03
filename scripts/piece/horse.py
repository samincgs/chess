from .piece import Piece

class Horse(Piece):
    def __init__(self, pos, color):
        self.type = 'horse'
        super().__init__(pos, color)