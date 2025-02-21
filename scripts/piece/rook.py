from .piece import Piece

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.type = 'rook'
        print(f'data/images/{self.color}/{self.type}.png')
        
        
    