from .piece import Piece

class Pawn(Piece):
    def __init__(self, pos, color):
        self.type = 'pawn'
        super().__init__(pos, color)
        
        self.direction = 1 if color == 'black' else -1
        
    def show_moves(self):
        return [[self.pos[0], self.pos[1] + self.direction]]