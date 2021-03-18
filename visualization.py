from brain import *
from map import *
from utils import *

import pygame
import time

map = Map()
brain = Brain()

screen = pygame.display.set_mode([map.w*20, map.h*20])

pygame.init()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    for cell in map.snake:
        pygame.draw.rect(screen, (0, 255, 0), (cell[0]*20, cell[1]*20, 20,20))

    for cell in map.walls:
        pygame.draw.rect(screen, (0, 0, 0), (cell[0]*20, cell[1]*20, 20,20))

    cell = map.apple
    pygame.draw.rect(screen, (255, 0, 0), (cell[0]*20, cell[1]*20, 20,20))

    dir = brain.predict_move(map)
    v = map.move(dir)
    if v is not None:
        print(v)
        break
    time.sleep(1/10)
    pygame.display.flip()