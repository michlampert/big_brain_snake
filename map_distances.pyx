# distutils: language = c++

from utils import *
from itertools import count

from libcpp.vector cimport vector
from libcpp.set cimport set
from libcpp.pair cimport pair

def add_vectors(pair[int,int] v1, pair[int,int] v2):
    cdef pair[int,int] p = (v1.first+v2.first, v1.second+v2.second)
    return p

def mul_vector(pair[int,int] v, int n):
    cdef pair[int,int] p = (v.first*n, v.second*n)
    return p

def distances(set[pair[int,int]] walls, list v_snake, pair[int,int] apple):
    cdef pair[int,int] snake0 = v_snake[0]
    cdef set[pair[int,int]] snake = v_snake[1:]

    wall_distances = []

    for dir in ALL_DIRECTIONS:
        for i in count(0):
            v = mul_vector(dir, i)
            if walls.count(add_vectors(snake0, v)) > 0:
                wall_distances.append(i)
                break

    snake_distances = []
    for dir in ALL_DIRECTIONS:
        for i in count(0):
            v = mul_vector(dir, i)
            if walls.count(add_vectors(snake0, v)) > 0 or snake.count(add_vectors(snake0, v)) > 0:
                snake_distances.append(i)
                break

    apple_distance = add_vectors(apple, mul_vector(snake0,-1))

    return wall_distances + snake_distances + list(apple_distance)
       