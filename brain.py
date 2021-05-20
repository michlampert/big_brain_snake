from map import * 
from utils import *
import random
import pickle
import math
import numpy as np
from functools import reduce

def id(x): return x

def sqrt(x): return np.sqrt(np.abs(x)) * np.sign(x)

def sigmoid(x): return 1/(1-np.exp(-x))

def relu(x): return x * (x > 0)

class Brain:
    def __init__(self, matrices=None, functions=None, v=None):
        """
        Genotype should be 12 values vector approx. between -1 and 1.
        Note that weights in NN should have some symmetry, because:
            - side directions should have the same meaning
            - output directions neurons should be linear combination of the same values, but turned 90deg
        That's why we can have only 12 different values instead of 4x18, what caused slow convergence.
        (https://en.wikipedia.org/wiki/Curse_of_dimensionality)
        """


        # shapes = [(12,6), (6,4), (4,1)]
        shapes = [(12,4), (4,1)]

        if not matrices:
            matrices = [np.random.rand(*shape)*2-1 for shape in shapes]

        if not functions:
            functions = [sqrt, sigmoid, sigmoid]

        self.matrices = matrices
        self.functions = functions

        if not v: v = [random.random() * 2 - 1 for i in range(12)]
        self.v = v

        self.local_best = None

    @staticmethod
    def dist_to_matrix(dist):
        w_u, w_ru, w_r, w_rd, w_d, w_ld, w_l, w_lu, s_u, s_ru, s_r, s_rd, s_d, s_ld, s_l, s_lu, a_x, a_y = dist


        dist_matrix = np.array([
            [w_u, (w_ru+w_lu)/2, (w_r+w_l)/2, (w_rd+w_ld)/2, w_d, s_u, (s_ru+s_lu)/2, (s_r+s_l)/2, (s_rd+s_ld)/2, s_d, a_x, a_y],
            [w_r, (w_ru+w_rd)/2, (w_u+w_d)/2, (w_lu+w_ld)/2, w_l, s_r, (s_ru+s_rd)/2, (s_u+s_d)/2, (s_lu+s_ld)/2, s_l, -a_y, a_x],
            [w_d, (w_rd+w_ld)/2, (w_r+w_l)/2, (w_ru+w_lu)/2, w_u, s_d, (s_rd+s_ld)/2, (s_r+s_l)/2, (s_ru+s_lu)/2, s_u, -a_x, -a_y],
            [w_l, (w_lu+w_ld)/2, (w_u+w_d)/2, (w_ru+w_rd)/2, w_r, s_l, (s_lu+s_ld)/2, (s_u+s_d)/2, (s_ru+s_rd)/2, s_r, a_y, -a_x]
        ])

        return dist_matrix

    def predict_move(self, map):
        dist = map.get_distances()
        dist_matrix = Brain.dist_to_matrix(dist)

        res = dist_matrix

        for m, f in zip(self.matrices, self.functions):
            res = res @ f(m)

        res = res.T[0].tolist()

        for i in range(4):
            if res[i] == max(res):
                return [UP, RIGHT, DOWN, LEFT][i]

    @staticmethod
    def random_gene(m1, m2):
        mr = np.random.randint(2, size=m1.shape)
        return mr*m1 + (1-mr)*m2

    @staticmethod
    def random_weighted_gene(m1, m2):
        mr = np.random.randint(2, size=m1.shape) * np.random.randint(2, size=m1.shape)
        return mr*m2 + (1-mr)*m1

    @staticmethod
    def between_gene(m1, m2):
        return (m1+m2)/2

    @staticmethod
    def between_weighted_gene(m1, m2, ratio=2/3):
        return m1*ratio + m2*(1-ratio)

    def cross(self, other, new_gene_func = random_gene):
        matrices = [new_gene_func(m1,m2) for m1,m2 in zip(self.matrices, other.matrices)]
        return Brain(matrices, self.functions)

    def mutate(self):
        self.matrices = [m1*(np.random.rand(*m1.shape)*0.2 + 0.9) for m1 in self.matrices]
        return self

    def pso(self, best, w=0.1, c1=1.2, c2=1.2, result=0):
        if self is best: return self

        if self.local_best:
            r, _ = self.local_best
            if r<result:
                self.local_best = result, self.matrices
        else:
            self.local_best = result, self.matrices

        _, local_best_matrices = self.local_best
        global_best_matrices = best.matrices
        
        lr = 0.5
        r1 = random.random()
        r2 = random.random()
        new_v = lambda m_v, x, m_lb, m_gb: m_v * w + (m_lb - x) * r1 * c1 + (m_gb - x) * r2 * c2 
        self.v = [new_v(m_v, x, m_lb, m_gb) for m_v, x, m_lb, m_gb in zip(self.v, self.matrices, local_best_matrices, global_best_matrices)]
        self.matrices = [m_m + lr * m_v for m_m, m_v in zip(self.matrices, self.v)]
        
        return self

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



