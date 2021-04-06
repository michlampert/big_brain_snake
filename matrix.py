import random

class Matrix:
    def __init__(self, m=None, *,w=None, h=None, string=None):
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

    def T(self):
        return Matrix(list(map(list, zip(*self.m))))

    def mix(self, other):
        result = Matrix([[random.choice([self.m[r][c], other.m[r][c]])*(random.random()*0.1 + random.random()*0.1 + 0.9) for c in range(self.w)] for r in range(self.h)])
        return result

if __name__ == "__main__":
    m1 = Matrix(w=2, h=2)
    print(*m1.m,sep="\n")
    m2 = Matrix(w=2, h=2)
    print(*m2.m,sep="\n")
    
    print(*m1.mix(m2).m,sep="\n")