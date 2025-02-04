import pygame

from ..utils import load_image
from ..const import *

class Piece:
    def __init__(self, board, pos, color):
        self.board = board
        self.pos = list(pos)
        self.color = color
        self.image = load_image(IMG_PATH + color + '/' + self.type +'.png', alpha=True)
        self.selected = False
        self.moves = []
    
    def is_on_board(self, x, y):
        return 0 <= x <= 7 and 0 <= y <= 7
    
    def make_move(self, new_pos):
        self.pos = list(new_pos)
        
    def show_moves(self):
        pass
    
    
    def render(self, surf):
        surf.blit(self.image, (self.pos[0] * SIZE + RENDER_OFFSET, self.pos[1] * SIZE + RENDER_OFFSET))
        if self.moves:
            for move in self.moves:
                pygame.draw.circle(surf, (0, 0, 0), (move[0] * SIZE + SIZE // 2, move[1] * SIZE + SIZE // 2), 6)