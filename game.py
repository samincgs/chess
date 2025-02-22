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
        pygame.display.set_caption(CAPTION) # set caption
        
        self.clock = pygame.time.Clock() # clock to control FPS
        
        self.board = Board(self) # call the board class
        self.ui = UI(self)   # call the UI class
        
        self.mpos = None # declare var for the mpos
        self.chess_loc = None # declare var for the chess ranks 
        self.turn = [0, 'white'] # the first spot is number of total turns, second is whose turn it is
        
        self.selected_piece = None
        self.selected_pos = None
        
             
    def run(self):
        while True:
            self.display.fill(BG_COLOR) # sets the background of the screen

            self.board.render(self.display) # calls the render function from the Board class
        
            self.mpos = pygame.mouse.get_pos() # pygame function to get the current mouse position
            
            '''
             We divide by scale factor because we rendered our display to match the screen size,
             so if we had to multiply the width by 3 now we divide it by 3 to get the mouse position in the display,
             we also divide by SIZE to get the location of the individual tiles, since each chess tile is 24 pixels
             to get the location we divide it
             ex. mouse pos is in pixels so we divide by size to get tiles
             (100, 100) -> (100 / 24, 100 / 24) -> (4, 4) so it would be the 4th column 4th row
            '''
            self.mpos = (self.mpos[0] // SCALE_FACTOR // SIZE + 1, MAX_RANK - self.mpos[1] // SCALE_FACTOR // SIZE) 
            
            # here we check if the mouse position is bigger than the UI sidebar, if it is return None else give us the location
            if self.mpos[0] <= max(RANKS):
                self.chess_loc = (RANKS[self.mpos[0]] + str(self.mpos[1]))
                
            # game event loop
            for event in pygame.event.get():
                # if we click the x button on the top right of the game close the window
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # left click on mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # here we check if the mouse position is bigger than the UI sidebar, if it is return None else give us the location
                        if self.mpos[0] <= max(RANKS):
                            if self.selected_pos:
                                self.board.handle_click(self.chess_loc, move=True)
                            else:
                                self.board.handle_click(self.chess_loc, move=False)
                            print(self.chess_loc)
            
            # scale the display into the size of the screen so the pixel art gets scaled up
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            self.ui.render(self.screen) # draw the ui on the screen
            pygame.display.update() # reset game loop and update
            
            # control it to 60 FPS (not needed)
            dt = self.clock.tick(FPS)

# run the main game file  
if __name__ == '__main__':
    Game().run()
            

