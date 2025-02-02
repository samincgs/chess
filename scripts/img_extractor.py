import pygame
import os
from utils import load_image, clip

IMG_PATH = 'data/images/'
IMG_SIZE = 16
IMG_ORDER = ['king', 'queen', 'bishop', 'horse', 'rook', 'pawn']

pygame.init()
screen = pygame.display.set_mode((100, 100))

chess_sheet = load_image(IMG_PATH + 'pieces.png', alpha=True)

if not os.path.isdir(IMG_PATH + 'black'):
    os.mkdir(IMG_PATH + 'black')
    
if not os.path.isdir(IMG_PATH + 'white'):
    os.mkdir(IMG_PATH + 'white')

for y in range(chess_sheet.get_height() // IMG_SIZE):
    for x in range(chess_sheet.get_width() // IMG_SIZE):
        sheet = clip(chess_sheet, (x * IMG_SIZE, y * IMG_SIZE), (IMG_SIZE, IMG_SIZE))
        if y == 0:
            pygame.image.save(sheet, IMG_PATH + 'black' + '/' + IMG_ORDER[x] + '.png', namehint='PNG')
        else:
            pygame.image.save(sheet, IMG_PATH + 'white' + '/' + IMG_ORDER[x] + '.png', namehint='PNG')