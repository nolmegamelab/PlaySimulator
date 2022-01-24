# test shape drawing 

import pygame
import sys 
import os

sys.path.insert(1, os.path.join(sys.path[0], '..'))

import scene.shape

pygame.init() 
pygame.display.set_caption('draw alpha')

screen = pygame.display.set_mode((1280, 768))
running = True 

c1 = scene.shape.Circle(100, 100, (255, 0, 0, 255), 30, 1)
c1.transform.move(100, 100)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(scene.shape.Color.WHITE)
    c1.draw(screen)
    pygame.display.flip()