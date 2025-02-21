import pygame

from ..utils import load_image
from ..const import *

class Piece:
    def __init__(self, board, color):
        self.board = board
        self.color = color # get the color from the self.tiles
        self.type = 'pawn'
        self.image = None
        self.load_piece()
    
    def load_piece(self):
        self.image = load_image(f'data/images/{self.color}/{self.type}.png', alpha=True)
    
    def render(self, surf, loc):
        if self.image:
            surf.blit(self.image, loc)
        