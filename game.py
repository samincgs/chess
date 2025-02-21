import pygame
import sys

from scripts.board import Board
from scripts.ui import UI
from scripts.const import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCALED_WIDTH, SCALED_HEIGHT))
        self.display = pygame.Surface((BASE_WIDTH, BASE_HEIGHT))
        pygame.display.set_caption(CAPTION)
        
        self.clock = pygame.time.Clock()
        
        self.board = Board(self)     
        self.ui = UI(self)   
        
        self.mpos = None
        self.chess_loc = None 
        self.turn = [0, 'white']
        
             
    def run(self):
        while True:
            self.display.fill(BG_COLOR)

            self.board.render(self.display)
        
            self.mpos = pygame.mouse.get_pos()
            self.mpos = (self.mpos[0] // SCALE_FACTOR // SIZE + 1, MAX_RANK - self.mpos[1] // SCALE_FACTOR // SIZE)  # +1 to make it 1 - 8, minus the y by 8 to invert it to give proper chess coords
            
            if self.mpos[0] <= max(RANKS):
                self.chess_loc = (RANKS[self.mpos[0]] + str(self.mpos[1]))
            else:
                self.chess_loc = None
                
            print(self.chess_loc)
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.board.handle_click(self.mpos)       
                  
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            self.ui.render(self.screen)
            pygame.display.update()
            dt = self.clock.tick(FPS)
            
if __name__ == '__main__':
    Game().run()
            

