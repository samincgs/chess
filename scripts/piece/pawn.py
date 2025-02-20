from .piece import Piece

class Pawn(Piece):
    def __init__(self, board, pos, color):
        self.type = 'pawn'
        super().__init__(board, pos, color)
        
        self.direction = 1 if color == 'black' else -1
        
    def make_move(self, new_pos):
        if self.board.first_pawn_move[self.color]:
            self.board.first_pawn_move[self.color] = False
        self.pos = list(new_pos)
    
    def show_moves(self):
        moves = []
        
        # moves twice on first turn
        if self.board.first_pawn_move[self.color]:
            step_count = 2
            for i in range(step_count):
                moves.append([self.pos[0], self.pos[1] + self.direction * (i + 1)])
        
        # normal turn
        else:
            moves = [[self.pos[0], self.pos[1] + self.direction]]
            
        # en passant
        
        # capture
        
        
        self.moves = moves
        