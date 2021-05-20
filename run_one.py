from map import *
from brain import *
from visualization import *

brain = Brain.from_file("saved_brains/saved_brains_14/gen_85")
map = Map()

v = Visualization(map, brain,save_frames=True)
v.start()
v.join()