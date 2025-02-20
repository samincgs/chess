# CONFIG
BASE_WIDTH = 192 + 80 # Extra 80 for UI
BASE_HEIGHT = 192
BOARD_SIZE = 192
SCALE_FACTOR = 3
SCALED_WIDTH = BASE_WIDTH * SCALE_FACTOR
SCALED_HEIGHT = BASE_HEIGHT * SCALE_FACTOR
CAPTION = 'Chess'
IMG_PATH = 'data/images/'
FONT_PATH = 'data/fonts/'
IMG_SIZE = 16
FPS = 60

# GAME VALUES
ROWS, COLS = 8, 8
SIZE = 24

BLACK_STARTING_POS = {
    (0, 0): 'rook',
    (1, 0): 'horse',
    (2, 0): 'bishop',
    (3, 0): 'queen',
    (4, 0): 'king',
    (5, 0): 'bishop',
    (6, 0): 'horse',    
    (7, 0): 'rook',
    (0, 1): 'pawn',
    (1, 1): 'pawn',
    (2, 1): 'pawn',
    (3, 1): 'pawn',
    (4, 1): 'pawn',
    (5, 1): 'pawn',
    (6, 1): 'pawn',    
    (7, 1): 'pawn',
}

WHITE_STARTING_POS = {
    (0, 7): 'rook',
    (1, 7): 'horse',
    (2, 7): 'bishop',
    (3, 7): 'queen',
    (4, 7): 'king',
    (5, 7): 'bishop',
    (6, 7): 'horse',    
    (7, 7): 'rook',
    (0, 6): 'pawn',
    (1, 6): 'pawn',
    (2, 6): 'pawn',
    (3, 6): 'pawn',
    (4, 6): 'pawn',
    (5, 6): 'pawn',
    (6, 6): 'pawn',    
    (7, 6): 'pawn',
}
RENDER_OFFSET = 4 # because size of square is diff from img size 

# COLORS
BG_COLOR = (46, 54, 109)
CHECKER_COLOR_1 = (202, 221, 240)
CHECKER_COLOR_2 = (89, 102, 187)
LINE_COLOR = (255, 255, 255)
SHADOW_COLOR = ''