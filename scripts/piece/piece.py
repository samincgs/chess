from ..utils import load_image
from ..const import *

class Piece:
    def __init__(self, pos, color):
        self.pos = list(pos)
        self.color = color
        self.image = load_image(IMG_PATH + color + '/' + self.type +'.png', alpha=True)
        
    
    def render(self, surf):
        surf.blit(self.image, (self.pos[0] * IMG_SIZE, self.pos[1] * IMG_SIZE))