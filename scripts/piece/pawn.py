from .piece import Piece

class Pawn(Piece):
    def __init__(self, board, color, pos):
        super().__init__(board, color, pos)
        self.type =  'pawn'
        self.load_piece()
        self.has_moved = False
        self.direction = 1 if self.color == 'white' else -1 # -1 GOES UP FOR WHITE, 1 GOES DOWN

    def get_moveset(self):
        moveset = []
        if self.has_moved == False:
            moveset.extend([(self.pos[0], self.pos[1] + self.direction), (self.pos[0], self.pos[1] + self.direction * 2)])
        else: # pawn has moved dumbass
             moveset.extend((self.pos[0], self.pos[1] + self.direction))
        
        return moveset