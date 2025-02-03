import pygame
import sys

from scripts.board import Board
from scripts.const import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCALED_WIDTH, SCALED_HEIGHT))
        self.display = pygame.Surface((BASE_WIDTH, BASE_HEIGHT))
        pygame.display.set_caption(CAPTION)
        
        self.clock = pygame.time.Clock()
        
        self.board = Board(self)
        self.pieces = []
        
        self.board.setup_board()
        
        self.click = False
        self.mpos = None
        
        self.first_turn = True
        self.turn = 'white'
        
        self.selected_piece = None
                
    def run(self):
        while True:
            self.display.fill((0, 0, 0))
                        
            self.board.update()
            self.board.render(self.display)
            
            if self.click and self.mpos in self.board.tiles:
                self.selected_piece = list(self.mpos)
            
            for piece in self.pieces:
                if self.selected_piece == piece.pos:
                    piece.selected = True
                else:
                    piece.selected = False
                    
                piece.update()
                piece.render(self.display)
            
            self.mpos = pygame.mouse.get_pos()
            self.mpos = (self.mpos[0] // SCALE_FACTOR // SIZE, self.mpos[1] // SCALE_FACTOR // SIZE)
                  
            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click = True

                
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)
            

if __name__ == '__main__':
    Game().run()
            

