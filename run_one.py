from map import *
from brain import *
from visualization import *

brain = Brain.from_file("saved_brains/saved_brains_7/gen_82")
map = Map()
# print(*brain.genotype.m)

v = Visualization(map, brain,save_frames=True)
v.start()
v.join()