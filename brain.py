from map import * 
from utils import *
import random
import pickle

from matrix import *

class Brain:
    def __init__(self, genotype=None):
        if genotype:
            if isinstance(genotype, list):
                self.genotype = Matrix([[i] for i in genotype])
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
        pass

    def mutate(self):
        pass
    
    # TODO
    def save(self, filename):
        with open(filename, "w+") as f:
            f.write(pickle.dumps(self.genotype))

    # TODO
    def from_file(self, filename):
        with open(filename) as f:
            self.genotype = pickle.loads(f.read())

if __name__ == "__main__":
    map = Map()
    brain = Brain()
    print(brain.predict_move(map))



