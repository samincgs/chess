import pygame
from .const import *
from .piece.bishop import Bishop
from .piece.rook import Rook
from .piece.horse import Horse
from .piece.queen import Queen
from .piece.king import King
from .piece.pawn import Pawn

CHESS_TYPES = {
    'rook': Rook,
    'horse': Horse,
    'bishop': Bishop,
    'queen': Queen,
    'king': King,
    'pawn': Pawn
}

class Board:
    def __init__(self, game):
        self.game = game
        self.tiles = {}
        
        self.pieces = []
        self.all_pos = []
                
        self.selected_piece = None
        
        self.setup_board()
    
    def setup_board(self): # make better later
        for pos, type in WHITE_STARTING_POS.items():
            self.pieces.append(CHESS_TYPES[type](self, pos, 'white'))
            
        for pos, type in BLACK_STARTING_POS.items():
            self.pieces.append(CHESS_TYPES[type](self, pos, 'black'))
    
    def get_piece_at(self, pos):
        for piece in self.pieces:
            if piece.pos == list(pos):
                return piece
        return None
    
    def reset_pieces(self, all_pieces):
        for piece in all_pieces:
            piece.moves = []
     
    def handle_click(self, pos):
        clicked_pos = self.get_piece_at(pos)
        
        if pos in self.tiles:
            if clicked_pos and clicked_pos.color == self.game.turn[1]:
                
                # reset all the pieces shown moves
                self.reset_pieces()
                
                # show all current pieces moves
                clicked_pos.show_moves()
                
                if self.selected_piece != clicked_pos:
                    self.selected_piece = clicked_pos
                    return
        
        if self.selected_piece:
            if list(pos) in self.selected_piece.moves:
                self.selected_piece.make_move(pos)
                self.selected_piece.moves = []
                self.selected_piece = None
                self.game.turn[0] += 1
                self.game.turn[1] = 'black' if self.game.turn[1] == 'white' else 'white'
                
        
        
    def render(self, surf):
        c = 0
        for y in range(ROWS):
            c = 0 if c != 0 else 1
            for x in range(COLS):
                r = pygame.Rect(x * SIZE, y * SIZE, SIZE, SIZE)
                if c == 0:
                    color = CHECKER_COLOR_1
                    c = 1
                else:
                    color = CHECKER_COLOR_2
                    c = 0
                if (x, y) not in self.tiles:
                    self.tiles[(x, y)] = r
                pygame.draw.rect(surf, color, r)
        
        
        for piece in self.pieces:
            piece.render(surf)
        
        # line seperator
        pygame.draw.line(surf, LINE_COLOR, (192, 0), (192, 192))
                