import random

class Matrix:
    def __init__(self, m=None, w=None, h=None, string=None):
        if string:
            m = eval(string)
        elif m is None:
            m = [[random.random()*2 - 1 for c in range(w)] for r in range(h)]
        self.m = m
        self.h = len(self.m)
        self.w = len(self.m[0])

    def __mul__(self, other:list):
        result = [0] * self.h
        for r in range(self.h):
            for c in range(self.w):
                result[r] += self.m[r][c] * other[c]
        return result