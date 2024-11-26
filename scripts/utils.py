import pygame
import os

BASE_IMP_PATH = 'assets/'

def load_image(path):
    img = pygame.image.load(BASE_IMP_PATH + path)
    # img.set_colorkey((255,255,255))
    return img

def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMP_PATH + path)):
        images.append(load_image(path + '/' + img_name))
    return images