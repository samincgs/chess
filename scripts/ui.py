import pygame

from .const import *

class UI: # UI class
    def __init__(self, game):
        self.game = game
        self.fonts = {} # store all the fonts we use
        
        self.load_fonts()
        
        
    def load_fonts(self):
        self.fonts['lato_regular'] = pygame.font.Font(FONT_PATH + '/' + 'lato_regular.ttf', 26) # path of the font, size of the font (change size to fit ur needs)
        self.fonts['lato_medium'] = pygame.font.Font(FONT_PATH + '/' + 'lato_medium.ttf', 24)
        self.fonts['lato_bold'] = pygame.font.Font(FONT_PATH + '/' + 'lato_bold.ttf', 24)
    

    def render(self, surf): # render the font into the screen
        text = self.fonts['lato_regular'].render('Turn: ' + str(self.game.turn[0]), True, WHITE_COLOR) # text, antialiasing, color
        surf.blit(text, (BOARD_SIZE * 3 + 5, 0)) # text is the font and the text surface and next is the location