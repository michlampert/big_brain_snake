from map import *
from brain import *
from visualization import *

brain = Brain.from_file("saved_brains/saved_brains_7/gen_99")
map = Map()

v = Visualization(map, brain,save_frames=False)
v.start()
v.join()