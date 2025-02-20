import pygame

from .const import *


class UI:
    def __init__(self, game):
        self.game = game
        self.fonts = {}
        
        self.load_fonts()
        
        
    def load_fonts(self):
        self.fonts['lato_regular'] = pygame.font.Font(FONT_PATH + '/' + 'lato_regular.ttf', 26)
        self.fonts['lato_medium'] = pygame.font.Font(FONT_PATH + '/' + 'lato_medium.ttf', 24)
        self.fonts['lato_bold'] = pygame.font.Font(FONT_PATH + '/' + 'lato_bold.ttf', 24)
    
    
    def render(self, surf):
        text = self.fonts['lato_regular'].render('Turn: ' + str(self.game.turn[0]), True, (255, 255, 255))
        surf.blit(text, (BOARD_SIZE * 3 + 5, 0))