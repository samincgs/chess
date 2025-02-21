from .piece import Piece

class Horse(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.type =  'horse'