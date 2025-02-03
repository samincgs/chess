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
                
    def run(self):
        while True:
            self.display.fill((0, 0, 0))
            
            self.board.render(self.display)
            
            for piece in self.pieces:
                piece.render(self.display)
                        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)
            

if __name__ == '__main__':
    Game().run()
            

