import pandas as pd
import matplotlib.pyplot as plt

for i in range(14,35):
    try:

        filename = f"logs_{i}"

        result = []
        with open(filename + ".txt") as f:
            for line in f:
                t = line.replace("|"," ").replace("\t", "").replace("\n","").split(" ")
                t = tuple(float(el) for el in t if el.replace(".","").isdigit())
                # t = (t[1],t[4],t[6])
                result.append(t)

        df = pd.DataFrame(result, columns=["best", "top 20", "generation"])
        df.plot()

        plt.xlabel("numer generacji")
        plt.ylabel("uzyskany wynik")
        plt.savefig(filename+".png")
    except Exception as e:
        pass