from map import *
from brain import *
from visualization import *


brains = [Brain() for i in range(1024)]

for i in range(100):

    d = [(brain,Map.calculte_expected_result(brain,probe=5)) for brain in brains]

    d.sort(key=lambda p: p[1], reverse=True)

    d[0][0].save(f"saved_brains/gen_{i}")

    print(f"gen {i} best score: {d[0][1]}\t|\tgen {i} best 32 scores mean: {sum(list(map(lambda p: p[1], d))[:32])/32}\t|\tgen {i} mean: {sum(list(map(lambda p: p[1], d)))/len(d)}")

    next_stage_brains = list(map(lambda p: p[0], d))[:32]


    brains = [b1.cross(b2) for b1 in next_stage_brains for b2 in next_stage_brains if b1 is not b2] + next_stage_brains

# brain = Brain.from_file("saved_brains/gen_5")
# map = Map()
# v = Visualization(map,brain)
# v.start()
# v.join()

# brain = Brain.from_file("saved_brains/gen_6")
# map = Map()
# v = Visualization(map,brain)
# v.start()
# v.join()

# brain = Brain.from_file("saved_brains/gen_7")
# map = Map()
# v = Visualization(map,brain)
# v.start()
# v.join()

# brain = Brain.from_file("saved_brains/gen_8")
# map = Map()
# v = Visualization(map,brain)
# v.start()
# v.join()

# brain = Brain.from_file("saved_brains/gen_9")
# map = Map()
# v = Visualization(map,brain)
# v.start()
# v.join()


