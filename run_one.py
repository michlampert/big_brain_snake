from map import *
from brain import *
from visualization import *

brain = Brain.from_file("saved_brains/saved_brains_14/gen_85")
map = Map(50,12)

v = Visualization(map, brain,save_frames=False)
v.start()
v.join()