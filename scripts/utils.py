import pygame

# UTILITY Functions used in our code

def load_image(path, colorkey=None, alpha=False):
    img = pygame.image.load(path).convert() if not alpha else pygame.image.load(path).convert_alpha()
    if colorkey:
        img.set_colorkey(colorkey)
    return img

def clip(surf, loc, size):
    handle_surf = surf.copy()
    rect = pygame.Rect(*loc, *size)
    handle_surf.set_clip(rect)
    img = surf.subsurface(handle_surf.get_clip())
    return img
    