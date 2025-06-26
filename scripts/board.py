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
        
    

                
                