from brain import *
from utils import *
import random

class Map:
    def __init__(self, w = 20, h = 20):
        self.w = w
        self.h = h
        self.walls = [(0, i-1) for i in range(w)] + [(i-1, 0) for i in range(h)] + [(h-1, i) for i in range(w)] + [(i, w-1) for i in range(h)]
        self.snake = [(random.randint(1,w-2), random.randint(1,h-2))]
        self.apple = (random.randint(1,w-2), random.randint(1,h-2))

    def move(self, direction):
        """return actual poins and game_over flag"""
        next_cell = (self.snake[0][0] + direction[0], self.snake[0][1] + direction[1])

        if self.snake[0] in self.walls + self.snake[1:]:
            return len(self.snake) - 1, True

        if self.apple in self.snake:
            while self.apple in self.snake:
                self.apple = (random.randint(1,self.w-2), random.randint(1,self.h-2))
        else:
            self.snake.pop()

        self.snake = [next_cell] + self.snake
        return len(self.snake) - 1, False

    def restart(self):
        self.snake = [(random.randint(1,self.w-2), random.randint(1,self.h-2))]
        

