from map import *
from brain import *
from visualization import *


for iteration in [14,19,15,17,25,26,30]:
    filename = f"saved_brains/saved_brains_{iteration}"

    print(f"results for saved brains {iteration}")

    n=90

    sum = 0
    for i in range(n,n+10):
        brain = Brain.from_file(f"{filename}/gen_{i}")
        sum += Map.calculte_expected_result(brain, 20,20,20)

    print("20x20", "&", round(sum/10,2), "\\\\")

    sum = 0
    for i in range(n,n+10):
        brain = Brain.from_file(f"{filename}/gen_{i}")
        sum += Map.calculte_expected_result(brain, 12,12,20)

    print("12x12", "&", round(sum/10,2), "\\\\")

    sum = 0
    for i in range(n,n+10):
        brain = Brain.from_file(f"{filename}/gen_{i}")
        sum += Map.calculte_expected_result(brain, 30,30,20)

    print("30x30", "&", round(sum/10,2), "\\\\")

    sum = 0
    for i in range(n,n+10):
        brain = Brain.from_file(f"{filename}/gen_{i}")
        sum += Map.calculte_expected_result(brain, 25,15,20)

    print("25x15", "&", round(sum/10,2), "\\\\")
