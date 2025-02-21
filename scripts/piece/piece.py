import pygame

from ..utils import load_image
from ..const import *

class Piece:
    def __init__(self, color):
        self.color = color # get the color from the self.tiles
        self.type = 'pawn'
        self.image = load_image(f'data/images/{self.color}/{self.type}.png', alpha=True)
        
    
    
    def render(self, surf, loc):
        surf.blit(self.image, loc)
        