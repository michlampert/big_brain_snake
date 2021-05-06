import pandas as pd
import matplotlib.pyplot as plt

for i in [14]:

    filename = f"logs_{i}"

    result = []
    with open(filename + ".txt") as f:
        for line in f:
            t = line.replace("|"," ").replace("\t", "").replace("\n","").split(" ")
            t = tuple(float(el) for el in t if el.replace(".","").isdigit())
            # t = (t[1],t[4],t[6])
            result.append(t)

    df = pd.DataFrame(result, columns=["best", "next_stage", "generation"])
    df.plot()
    plt.savefig(filename+".png")