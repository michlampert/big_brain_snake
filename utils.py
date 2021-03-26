LEFT = (-1,0)
UP = (0,1)
RIGHT = (1,0)
DOWN = (0,-1)
LU = (-1,1)
RU = (1,1)
LD = (-1,-1)
RD = (1,-1)
ALL_DIRECTIONS = [LEFT,LU,UP,RU,RIGHT,RD,DOWN,LD]

def add_vectors(v1, v2):
    return (v1[0]+v2[0], v1[1]+v2[1])

def mul_vector(v,n):
    return (v[0]*n, v[1]*n)
