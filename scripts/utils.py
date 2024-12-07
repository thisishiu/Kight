import pygame
import os

BASE_IMP_PATH = 'assets/'

import pygame
import os

def load_image(path, colorkey=None):
    path = BASE_IMP_PATH + path
    try:
        image = pygame.image.load(os.path.join(path)).convert_alpha()
    except pygame.error as e:
        print(f"Can not load the image: {path}")
        raise SystemExit(e)
    
    if colorkey is not None:
        image.set_colorkey(colorkey)
    
    return image


def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMP_PATH + path)):
        images.append(load_image(path + '/' + img_name))
    return images