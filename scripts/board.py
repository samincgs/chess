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
            'a1': Rook(self, 'white', self.get_pos('a1')), 'b1': Horse(self, 'white', self.get_pos('b1')), 'c1': Bishop(self, 'white', self.get_pos('c1')), 'd1': Queen(self, 'white', self.get_pos('d1')), 'e1': King(self, 'white', self.get_pos('e1')), 'f1': Bishop(self, 'white', self.get_pos('f1')), 'g1': Horse(self, 'white', self.get_pos('g1')), 'h1': Rook(self, 'white', self.get_pos('h1')),
            'a2': Pawn(self, 'white', self.get_pos('a2')), 'b2': Pawn(self, 'white', self.get_pos('b2')), 'c2': Pawn(self, 'white', self.get_pos('c2')), 'd2': Pawn(self, 'white', self.get_pos('d2')), 'e2': Pawn(self, 'white', self.get_pos('e2')), 'f2': Pawn(self, 'white', self.get_pos('f2')), 'g2': Pawn(self, 'white', self.get_pos('g2')), 'h2': Pawn(self, 'white', self.get_pos('h2')),
            'a3': None, 'b3': None, 'c3': None, 'd3': None, 'e3': None, 'f3': None, 'g3': None, 'h3': None,
            'a4': None, 'b4': None, 'c4': None, 'd4': None, 'e4': None, 'f4': None, 'g4': None, 'h4': None,
            'a5': None, 'b5': None, 'c5': None, 'd5': None, 'e5': None, 'f5': None, 'g5': None, 'h5': None,
            'a6': None, 'b6': None, 'c6': None, 'd6': None, 'e6': None, 'f6': None, 'g6': None, 'h6': None,
            'a7': Pawn(self, 'black', self.get_pos('a7')), 'b7': Pawn(self, 'black', self.get_pos('b7')), 'c7': Pawn(self, 'black', self.get_pos('c7')), 'd7': Pawn(self, 'black', self.get_pos('d7')), 'e7': Pawn(self, 'black', self.get_pos('e7')), 'f7': Pawn(self, 'black', self.get_pos('f7')), 'g7': Pawn(self, 'black', self.get_pos('g7')), 'h7': Pawn(self, 'black', self.get_pos('h7')),
            'a8': Rook(self, 'black', self.get_pos('a8')), 'b8': Horse(self, 'black', self.get_pos('b8')), 'c8': Bishop(self, 'black', self.get_pos('c8')), 'd8': Queen(self, 'black', self.get_pos('d8')),
            'e8': King(self, 'black', self.get_pos('e8')), 'f8': Bishop(self, 'black', self.get_pos('f8')), 'g8': Horse(self, 'black', self.get_pos('g8')), 'h8': Rook(self, 'black', self.get_pos('h8')),
        }
    
    
    # pos is the location in chess coords ('a1') and move is True if we are moving the piece else it is False if we are selecting a piece
    def handle_click(self, pos, move):
        for notation, piece in self.tiles.items():
            if notation == pos:
                self.game.selected_tile = pos

                if piece:
                    self.game.selected_piece = piece
                    print(piece.get_moveset())
            else:
                self.game.selected_tile = None
                self.game.selected_piece = None

        
        pass
          
                    
    def render(self, surf):    
        # we use c to control which colors are white and which are blue    
        c = 1
        for y in range(1, 9): 
            c = 0 if c != 0 else 1 # switch the color on the alternate square
            for x in range(1, 9):
                r = pygame.Rect(y * SIZE - SIZE, x * SIZE - SIZE, SIZE, SIZE)
                if c == 0:
                    color = CHECKER_COLOR_1
                    c = 1
                else:
                    color = CHECKER_COLOR_2
                    c = 0
                pygame.draw.rect(surf, color, r) # draw the checkered rectangles
           
        # line seperator seperating the board and the ui
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
                piece.render(surf, ((self.get_pos(chess_pos)[0] - 1) * SIZE + RENDER_OFFSET, BOARD_SIZE - self.get_pos(chess_pos)[1] * SIZE + RENDER_OFFSET))

                
                