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
        head = self.snake[0]
        next_cell = (head[0] + direction[0], head[1] + direction[1])
        if next_cell in self.walls + self.snake:
            return len(self.snake)

        if head == self.apple:
            pass
        else:
            self.snake.pop()

        self.snake = [next_cell] + self.snake


        

