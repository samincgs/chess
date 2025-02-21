import pygame

from .const import *
from .piece.bishop import Bishop
from .piece.rook import Rook
from .piece.horse import Horse
from .piece.queen import Queen
from .piece.king import King
from .piece.pawn import Pawn

class Board:
    def __init__(self, game):
        self.game = game
        self.tiles = {}
        self.setup_board()
        
    def setup_board(self):
        self.tiles = {
            'a1': Rook('white'), 'b1': Horse('white'), 'c1': Bishop('white'), 'd1': Queen('white'), 'e1': King('white'), 'f1': Bishop('white'), 'g1': Horse('white'), 'h1': Rook('white'),
            'a2': Pawn('white'), 'b2': Pawn('white'), 'c2': Pawn('white'), 'd2': Pawn('white'), 'e2': Pawn('white'), 'f2': Pawn('white'), 'g2': Pawn('white'), 'h2': Pawn('white'),
            'a3': None, 'b3': None, 'c3': None, 'd3': None, 'e3': None, 'f3': None, 'g3': None, 'h3': None,
            'a4': None, 'b4': None, 'c4': None, 'd4': None, 'e4': None, 'f4': None, 'g4': None, 'h4': None,
            'a5': None, 'b5': None, 'c5': None, 'd5': None, 'e5': None, 'f5': None, 'g5': None, 'h5': None,
            'a6': None, 'b6': None, 'c6': None, 'd6': None, 'e6': None, 'f6': None, 'g6': None, 'h6': None,
            'a7': Pawn('black'), 'b7': Pawn('black'), 'c7': Pawn('black'), 'd7': Pawn('black'),'e7': Pawn('black'), 'f7': Pawn('black'), 'g7': Pawn('black'), 'h7': Pawn('black'),
            'a8': Rook('black'), 'b8': Horse('black'), 'c8': Bishop('black'), 'd8': Queen('black'),
            'e8': King('black'), 'f8': Bishop('black'), 'g8': Horse('black'), 'h8': Rook('black'),
        }
    
     
    def handle_click(self, pos):
        pass
                    
    def render(self, surf):        
        c = 1
        for y in range(8, 0, -1):
            c = 0 if c != 0 else 1
            for x in range(8, 0, -1):
                r = pygame.Rect(y * SIZE - SIZE, x * SIZE - SIZE, SIZE, SIZE)
                if c == 0:
                    color = CHECKER_COLOR_1
                    c = 1
                else:
                    color = CHECKER_COLOR_2
                    c = 0
                pygame.draw.rect(surf, color, r)
           
        # line seperator
        pygame.draw.line(surf, WHITE_COLOR, (BOARD_SIZE, 0), (BOARD_SIZE, BOARD_SIZE))
        
        
        for chess_pos, piece in self.tiles.items():
            if piece:
                piece = self.tiles[chess_pos]
                piece.render(surf, (CHESS_POSITIONS[chess_pos][0] * SIZE - SIZE + RENDER_OFFSET, CHESS_POSITIONS[chess_pos][1] * SIZE - SIZE + RENDER_OFFSET))
                
                