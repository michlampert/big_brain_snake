from map import Map
from brain import Brain
# from visualization import *


sqrt_num = 10

print(f"no | best | best {sqrt_num} | generation")
f = open("logs_13.txt", "w+")

brains = [Brain() for i in range(sqrt_num**2)]

for i in range(100):

    d = [(brain,Map.calculte_expected_result(brain,probe=10)) for brain in brains]

    d.sort(key=lambda p: p[1], reverse=True)

    d[0][0].save(f"saved_brains_13/gen_{i}")

    print(f"{i} | {d[0][1]} | {sum(list(map(lambda p: p[1], d))[:sqrt_num])/sqrt_num} | {sum(list(map(lambda p: p[1], d)))/len(d)}")
    print(f"{d[0][1]} | {sum(list(map(lambda p: p[1], d))[:sqrt_num])/sqrt_num} | {sum(list(map(lambda p: p[1], d)))/len(d)}", flush=True, file=f)

    next_stage_brains = list(map(lambda p: p[0], d))[:sqrt_num]

    brains = [b1.cross(b2, new_gene_func = Brain.random_gene).mutate() for b1 in next_stage_brains for b2 in next_stage_brains if b1 is not b2] + next_stage_brains

# f = open("logs_10.txt", "w+")

# for i in range(100):

#     d = [(brain,Map.calculte_expected_result(brain,probe=5)) for brain in brains]

#     d.sort(key=lambda p: p[1], reverse=True)

#     d[0][0].save(f"saved_brains_10/gen_{i}")

#     print(f"gen {i} best score: {d[0][1]}\t|\tgen {i} best {sqrt_num} scores mean: {sum(list(map(lambda p: p[1], d))[:sqrt_num])/sqrt_num}\t|\tgen {i} mean: {sum(list(map(lambda p: p[1], d)))/len(d)}")
#     print(f"gen {i} best score: {d[0][1]}\t|\tgen {i} best {sqrt_num} scores mean: {sum(list(map(lambda p: p[1], d))[:sqrt_num])/sqrt_num}\t|\tgen {i} mean: {sum(list(map(lambda p: p[1], d)))/len(d)}", flush=True, file=f)
    
#     brains = [b.pso(d[0][0], 0.2, 0.05) for b in brains]


