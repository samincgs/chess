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
        self.game = game # a reference to the game objects
        self.tiles = {} # holds all our tiles
        self.setup_board()
    
    # easy utility function to convert chess location to tile pos -> 'a1' -> (1, 1)
    def get_pos(self, chess_loc):
        return CHESS_POSITIONS[chess_loc]
        
    def setup_board(self):
        self.tiles = {
            'a1': Rook(self,'white'), 'b1': Horse(self,'white'), 'c1': Bishop(self,'white'), 'd1': Queen(self,'white'), 'e1': King(self,'white'), 'f1': Bishop(self,'white'), 'g1': Horse(self,'white'), 'h1': Rook(self,'white'),
            'a2': Pawn(self,'white'), 'b2': Pawn(self,'white'), 'c2': Pawn(self,'white'), 'd2': Pawn(self,'white'), 'e2': Pawn(self,'white'), 'f2': Pawn(self,'white'), 'g2': Pawn(self,'white'), 'h2': Pawn(self,'white'),
            'a3': None, 'b3': None, 'c3': None, 'd3': None, 'e3': None, 'f3': None, 'g3': None, 'h3': None,
            'a4': None, 'b4': None, 'c4': None, 'd4': None, 'e4': None, 'f4': None, 'g4': None, 'h4': None,
            'a5': None, 'b5': None, 'c5': None, 'd5': None, 'e5': None, 'f5': None, 'g5': None, 'h5': None,
            'a6': None, 'b6': None, 'c6': None, 'd6': None, 'e6': None, 'f6': None, 'g6': None, 'h6': None,
            'a7': Pawn(self,'black'), 'b7': Pawn(self,'black'), 'c7': Pawn(self,'black'), 'd7': Pawn(self,'black'),'e7': Pawn(self,'black'), 'f7': Pawn(self,'black'), 'g7': Pawn(self,'black'), 'h7': Pawn(self,'black'),
            'a8': Rook(self,'black'), 'b8': Horse(self,'black'), 'c8': Bishop(self,'black'), 'd8': Queen(self,'black'),
            'e8': King(self,'black'), 'f8': Bishop(self,'black'), 'g8': Horse(self,'black'), 'h8': Rook(self,'black'),
        }
    
     
    def handle_click(self, pos):
        pass
                    
    def render(self, surf):    
        # we use c to control which colors are white and which are blue    
        c = 1
        for y in range(8, 0, -1): # we go in opposite order from 8 all the way to 1 -> 8, 7, 6, 5 (because chess positions are a8 at the top and a1 at the bottom)
            c = 0 if c != 0 else 1 # switch the color on the alternate square
            for x in range(8, 0, -1): # we go in opposite order from 8 all the way to 1 -> 8, 7, 6, 5 
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
        
        # render all the chess pieces on the board
        for chess_pos, piece in self.tiles.items(): # get both the key and value of the self.tiles dictionary
            if piece: # check if a piece exists on a tile
                piece = self.tiles[chess_pos] # get the piece object (Rook, Queen, Pawn) whatever it is
                # call the render function and pass where its gonna be display and the loc
                ''' 
                the math is a bit confusing, first we get the position of the piece with chess_pos and pass it into our utility function to get the coordinate fr. (1, 1) or (2, 4) whatever
                then we multiply it by the size of each square which is 24 which gives us the location top left of each chess tile, then we add the render offset to centre it
                lastly we minus it from Board Size because we want it in the opposite directory (so it was being rendered a1 at the top a8 at the bottom but we minused it to flip the direction)
                this puts the white at the bottom and black at the top
                '''
                piece.render(surf, (BOARD_SIZE - self.get_pos(chess_pos)[0] * SIZE  + RENDER_OFFSET, BOARD_SIZE - self.get_pos(chess_pos)[1] * SIZE  + RENDER_OFFSET))
                
                