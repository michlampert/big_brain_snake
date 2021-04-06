from map import * 
from utils import *
import random
import pickle

from matrix import *

class Brain:
    def __init__(self, genotype=None):
        if genotype:
            if isinstance(genotype, list):
                self.genotype = Matrix(genotype)
            elif isinstance(genotype, Matrix):
                self.genotype = genotype
        else:
            self.genotype = Matrix(w=18,h=4)

    def predict_move(self, map):
        dist = map.get_distances()
        res = self.genotype * dist
        idx = -1
        for i in range(4):
            if res[i] == max(res):
                idx = i
        return [LEFT, UP, RIGHT, DOWN][idx]
        # return random.choice([LEFT, UP, RIGHT, DOWN])

    def cross(self, other):
        return Brain(self.genotype.mix(other.genotype))

    def mutate(self):
        pass

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



