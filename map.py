from brain import *
from utils import *
import random
from itertools import count

class Map:
    def __init__(self, w = 20, h = 20):
        self.w = w
        self.h = h
        self.walls = [(0, i-1) for i in range(w)] + [(i-1, 0) for i in range(h)] + [(h-1, i) for i in range(w)] + [(i, w-1) for i in range(h)]
        self.last_move = RIGHT
        self.snake = self.new_snake()
        self.apple = self.new_apple()
        self.live = 0

    def move(self, direction):
        """return actual poins and game_over flag"""
        next_cell = (self.snake[0][0] + direction[0], self.snake[0][1] + direction[1])

        if self.live == 100:
            return len(self.snake) - 3 + self.live/100, True  

        if self.apple in self.snake:
            self.live = 0
            while self.apple in self.snake:
                self.apple = self.new_apple()
        else:
            self.snake.pop()

        self.snake = [next_cell] + self.snake

        if self.snake[0] in self.walls + self.snake[1:]:
            return len(self.snake) - 3 + self.live/100, True

        self.live += 1
        return len(self.snake) - 3 + self.live/100, False

    def restart(self):
        self.snake = self.new_snake()
        self.apple = self.new_apple()
        self.live = 0

    def new_apple(self):
        apple = None
        while not apple or apple in self.snake:
                apple = (random.randint(1,self.w-2), random.randint(1,self.h-2))
        return apple

    def new_snake(self):
        snake = [(random.randint(2,self.w-3), random.randint(2,self.h-3))]*3
        # snake.append(add_vectors(snake[0], mul_vector(self.last_move, -1)))
        return snake

    def get_distances(self):
        """return list of distances to walls [<,\,^,/,>,\\,v,/], snake [<,\,^,/,>,\\,v,/] and apple [x,y]"""

        wall_distances = []
        for dir in ALL_DIRECTIONS:
            for i in count(0):
                v = mul_vector(dir, i)
                if add_vectors(self.snake[0], v) in self.walls:
                    wall_distances.append(i)
                    break

        snake_distances = []
        for dir in ALL_DIRECTIONS:
            for i in count(0):
                v = mul_vector(dir, i)
                if add_vectors(self.snake[0], v) in self.walls + self.snake[1:]:
                    snake_distances.append(i)
                    break

        apple_distance = add_vectors(self.apple, mul_vector(self.snake[0],-1))

        return wall_distances + snake_distances + list(apple_distance)

    def calculte_expected_result(brain, w=20, h=20, probe=100):
        """return expected points result with usage of this brain"""
        result = 0
        for i in range(probe):
            map = Map(w,h)
            end = False
            while not end:
                dir = brain.predict_move(map)
                points, end = map.move(dir)
            result += points
        return result/probe

if __name__ == "__main__":
    brain = Brain()
    print(Map.calculte_expected_result(brain))

        

