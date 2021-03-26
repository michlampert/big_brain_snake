from brain import *
from map import *
from utils import *

import pygame
import time
import threading
import itertools

import sys

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

class HumanInput(Brain):
    def __init__(self):
        pass

    def predict_move(self, map: Map, *args, **kwargs):
        dir = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    dir = LEFT
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    dir = UP
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    dir = RIGHT
                if event.key == pygame.K_UP or event.key == ord('w'):
                    dir = DOWN

        return dir

class Visualization(threading.Thread):
    def __init__(self, map: Map, brain: Brain, save_frames=False):
        threading.Thread.__init__(self)
        self.map = map
        self.brain = brain
        self.save_frames = save_frames

    def run(self):
        screen = pygame.display.set_mode([self.map.w*20, self.map.h*20])

        pygame.init()
        dir = RIGHT
        frames = itertools.count(1000)

        while True:
            dir = self.brain.predict_move(self.map) or dir

            points, end = self.map.move(dir)

            # drawing part

            screen.fill((255, 255, 255))

            for cell in self.map.walls:
                pygame.draw.rect(screen, (0, 0, 0), (cell[0]*20, cell[1]*20, 20,20))

            cell = self.map.apple
            pygame.draw.rect(screen, (200, 0, 0), (cell[0]*20, cell[1]*20, 20,20))

            for cell in self.map.snake:
                pygame.draw.rect(screen, (0, 200, 0), (cell[0]*20, cell[1]*20, 20,20))

            cell = self.map.snake[0]
            pygame.draw.rect(screen, (0, 150, 0), (cell[0]*20, cell[1]*20, 20,20))
                
            cell = (self.map.snake[0][0] + dir[0], self.map.snake[0][1] + dir[1])
            pygame.draw.circle(screen, (240, 240, 240), (cell[0]*20 + 10, cell[1]*20 + 10), 5)

            textsurface = myfont.render(str(points), False, (255, 255, 255))
            screen.blit(textsurface,(5,0))

            for cell in [add_vectors(self.map.snake[0],mul_vector(v, i)) for i, v in zip(self.map.get_distances(), ALL_DIRECTIONS*2)]:
                pygame.draw.circle(screen, (0,0, 255), (cell[0]*20 + 10, cell[1]*20 + 10), 5)

            if self.save_frames: 
                pygame.image.save(screen, f"tmp/frame{next(frames)}.png")

            pygame.display.flip()

            # ----

            if end:
                time.sleep(1)
                if isinstance(self.brain, HumanInput):
                    self.map.restart()
                else:
                    print(points)
                    break
            time.sleep(1/10)

map = Map()
brain = Brain()
brain = HumanInput()

V = Visualization(map, brain, save_frames=False)
V.start()

"""
to convert frames into .gif:
    $ convert -delay 10 tmp/*.png demo.gif
    $ rm tmp/* -f
"""