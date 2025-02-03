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
        
    def setup_board(self): # make better later
        for pos, type in WHITE_STARTING_POS.items():
            color = 'white'
            if type == 'rook':
                self.game.pieces.append(Rook(pos, color))
            elif type == 'horse':
                self.game.pieces.append(Horse(pos, color))
            elif type == 'bishop':
                self.game.pieces.append(Bishop(pos, color))
            elif type == 'queen':
                self.game.pieces.append(Queen(pos, color))
            elif type == 'king':
                self.game.pieces.append(King(pos, color))
            else:
                self.game.pieces.append(Pawn(pos, color))
        
        for pos, type in BLACK_STARTING_POS.items():
            color = 'black'
            if type == 'rook':
                self.game.pieces.append(Rook(pos, color))
            elif type == 'horse':
                self.game.pieces.append(Horse(pos, color))
            elif type == 'bishop':
                self.game.pieces.append(Bishop(pos, color))
            elif type == 'queen':
                self.game.pieces.append(Queen(pos, color))
            elif type == 'king':
                self.game.pieces.append(King(pos, color))
            else:
                self.game.pieces.append(Pawn(pos, color))
              
    
    def update(self):
        pass
        
          
    def render(self, surf):
        c = 0
        for y in range(ROWS):
            c = 0 if c != 0 else 1
            for x in range(COLS):
                r = pygame.Rect(x * SIZE, y * SIZE, SIZE, SIZE)
                if c == 0:
                    color = (127, 127, 127)
                    c = 1
                else:
                    color = (255, 255, 255)
                    c = 0
                if (x, y) not in self.tiles:
                    self.tiles[(x, y)] = r
                pygame.draw.rect(surf, color, r)
                
        
        # line seperator
        pygame.draw.line(surf, (255, 0, 0), (192, 0), (192, 192))
                