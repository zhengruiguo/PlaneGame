import pygame
from pygame.locals import *
for event in pygame.event.get():
    if event.type == QUIT:
        print('exit')
        exit()
    elif event.type == KEYDOWN:
        if event.key == K_a or event.key == K_LEFT:
            print('left')
        elif event.key == k_d or event.key == K_RIGHT:
            print('right')
        elif event.key == K_SPACE:
            print('space')
