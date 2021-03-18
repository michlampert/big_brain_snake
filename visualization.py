from brain import *
from map import *
from utils import *

import pygame
import time
import threading
import itertools

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

class Visualization(threading.Thread):
    def __init__(self, map, brain = None, save_frames=False):
        threading.Thread.__init__(self)
        self.map = map
        self.brain = brain
        self.save_frames = save_frames

    def run(self):
        map = self.map
        brain = self.brain
        screen = pygame.display.set_mode([map.w*20, map.h*20])

        pygame.init()
        dir = RIGHT
        running = True
        frames = itertools.count(1000)
        while running:

            

            screen.fill((255, 255, 255))
            for cell in map.snake:
                pygame.draw.rect(screen, (0, 255, 0), (cell[0]*20, cell[1]*20, 20,20))

            for cell in map.walls:
                pygame.draw.rect(screen, (0, 0, 0), (cell[0]*20, cell[1]*20, 20,20))

            cell = map.apple
            pygame.draw.rect(screen, (255, 0, 0), (cell[0]*20, cell[1]*20, 20,20))

            if brain is not None:  
                dir = brain.predict_move(map)

                cell = (map.snake[0][0] + dir[0], map.snake[0][1] + dir[1])
                pygame.draw.rect(screen, (230, 230, 230), (cell[0]*20, cell[1]*20, 20,20))
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT or event.key == ord('a'):
                            dir = LEFT
                        if event.key == pygame.K_DOWN or event.key == ord('s'):
                            dir = UP
                        if event.key == pygame.K_RIGHT or event.key == ord('d'):
                            dir = RIGHT
                        if event.key == pygame.K_UP or event.key == ord('w'):
                            dir = DOWN

            v, end = map.move(dir)
            textsurface = myfont.render(str(v), False, (255, 255, 255))
            screen.blit(textsurface,(5,0))

            if self.save_frames: 
                pygame.image.save(screen, f"tmp/frame{next(frames)}.png")

            if end:
                print(v)
                break
            time.sleep(1/10)
            pygame.display.flip()
        pygame.display.flip()
        time.sleep(1)



map = Map()
brain = Brain()

V = Visualization(map, brain, save_frames=True)
V.start()

# import os

# os.system("convert -delay 10 tmp/*.png demo.gif")
# os.system("rm tmp/* -f")