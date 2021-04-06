from map import *
from brain import *
from visualization import *

brain = Brain.from_file("saved_brains_2/gen_19")
map = Map()
# print(*brain.genotype.m)

v = Visualization(map, brain,save_frames=True)
v.start()
v.join()