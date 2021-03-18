from map import *
from utils import *
import random

class Brain:
    def __init__(self):
        pass

    def predict_move(self, map:Map):
        return random.choice([LEFT, UP, RIGHT, DOWN])

