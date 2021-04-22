from map import * 
from utils import *
import random
import pickle
import math

from matrix import *

class Brain:
    def __init__(self, genotype=None, v=None):
        """
        Genotype should be 12 values vector approx. between -1 and 1.
        Note that weights in NN should have some symmetry, because:
            - side directions should have the same meaning
            - output directions neurons should be linear combination of the same values, but turned 90deg
        That's why we can have only 12 different values instead of 4x18, what caused slow convergence.
        (https://en.wikipedia.org/wiki/Curse_of_dimensionality)
        """

        if not genotype:
            genotype = [random.random() * 2 - 1 for i in range(12)]

        self.genotype = genotype

        if isinstance(genotype, list):
            self.matrix = self.genotype_to_matrix()
        elif isinstance(genotype, Matrix):
            self.matrix = genotype
        if not v: v = [random.random() * 2 - 1 for i in range(12)]
        self.v = v

    def genotype_to_matrix(self):
        walls, snake, apple = self.genotype[:5], self.genotype[5:10], self.genotype[10:]
        walls = walls + walls[-2:0:-1]
        snake = snake + snake[-2:0:-1]
        x, y = apple

        return  Matrix([
                    [*walls, *snake, x, y],
                    [*(walls[-2:] + walls[:-2]),*(snake[-2:] + snake[:-2]), y, -x],
                    [*(walls[-4:] + walls[:-4]),*(snake[-4:] + snake[:-4]), -x, -y],
                    [*(walls[-6:] + walls[:-6]),*(snake[-6:] + snake[:-6]), -y, x]
                ])

    def predict_move(self, map):
        dist = map.get_distances()
        dist = [(0 if not d else (d/abs(d))*math.sqrt(abs(d))) for d in dist]
        res = self.matrix * dist
        idx = -1
        for i in range(4):
            if res[i] == max(res):
                idx = i
        return [LEFT, UP, RIGHT, DOWN][idx]

    @staticmethod
    def random_gene(g1, g2):
        return random.choice([g1,g2])

    @staticmethod
    def random_weighted_gene(g1, g2, ratio=2/3):
        return (g1 if (random.random() < ratio) else g2)

    @staticmethod
    def between_gene(g1, g2):
        return (g1+g2)/2

    @staticmethod
    def between_weighted_gene(g1, g2, ratio=2/3):
        return g1*ratio + g2*(1-ratio)

    def cross(self, other, new_gene_func = random_gene):
        return Brain([new_gene_func(g1,g2) for g1,g2 in zip(self.genotype, other.genotype)])

    def mutate(self):
        return Brain([g * (0.90 + (random.random() + random.random())/10) for g in self.genotype])

    def pso(self, best, w=0.1, c1=0.1):
        if self is best: return self
        r1 = random.random()
        v = [w*vx + c1*r1*(bx-gx) for vx,bx,gx in zip(self.v, best.genotype, self.genotype)]
        genotype = [gx + vx for gx,vx in zip(self.genotype,self.v)]
        return Brain(genotype,v)



    def save(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    def from_file(filename):
        with open(filename, "rb") as f:
            return pickle.load(f)

if __name__ == "__main__":
    map = Map()
    brain = Brain()
    print(brain.predict_move(map))



