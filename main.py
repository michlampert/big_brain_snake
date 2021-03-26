from map import *
from brain import *
from visualization import *

brains = [Brain() for i in range(1000)]

best = max(brains, key=lambda brain: Map.calculte_expected_result(brain,probe=3))

print(best.genotype.m)

with open("best","w+") as f:
    f.write(str(best.genotype.m))

with open("best") as f:
    best = Brain(genotype=Matrix(string=f.read()))

map = Map()
v = Visualization(map, best)
v.start()
v.join()

map = Map()
v = Visualization(map, best)
v.start()
v.join()

map = Map()
v = Visualization(map, best)
v.start()
v.join()

