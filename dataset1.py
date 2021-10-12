import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib #日本語対応
import random
import pandas as pd
from pandas.io.parsers import read_csv

"""
演習1.1
"""
def true_function(x):
    """
    >>> true_function(0)
    0
    """
    y = np.sin(np.pi * x * 0.8) * 10
    return y

"""
演習1.2
"""
def make_observe_points(mn, mx, seed=20):
    random.seed(seed)
    x = [random.uniform(mn,mx) for _ in range(20)]
    y = [true_function(i) for i in x]
    df = pd.DataFrame({"観測点": x, "真値": y})
    return df

"""
演習1.3
"""
def add_noizes(dataset, mean, ave):
    noizes = [np.random.normal(mean, ave) for _ in range(20)]
    noizes = [noize/2 for noize in noizes]
    y = dataset["真値"] + noizes
    dataset["観測値"] = y
    return dataset

"""
演習1.4
"""
def output_tsv_file(dataset, output_tsv_name):
    dataset.to_csv(output_tsv_name, sep="\t")

"""
演習1.5
"""
def read_tsv_file(file_path):
    df = pd.read_csv(file_path, sep="\t")
    return df

def draw_pictures(mn, mx):
    x = np.linspace(mn, mx, 100)
    y = true_function(x)
    plt.figure()
    plt.plot(x,y, label="y = sin(π * x * 0.8) * 10")
    plt.title("ex1.1")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend(loc="best")
    plt.savefig("ex1.1.png")

    dataset = make_observe_points(mn, mx)
    dataset = add_noizes(dataset, 0, 2)
    plt.title("ex1.2")
    plt.scatter(dataset["観測点"].values, dataset["真値"].values, label="真値")
    plt.legend(loc="best")
    plt.savefig("ex1.2.png")

    plt.title("ex1.3")
    plt.scatter(dataset["観測点"].values, dataset["観測値"].values, label="観測値")
    plt.legend(loc="best")
    plt.savefig("ex1.3.png")

if __name__ == "__main__":
    mn = -1
    mx = 1
    dataset = make_observe_points(mn, mx)
    dataset = add_noizes(dataset, 0, 2)

    draw_pictures(mn, mx)

    output_tsv_file(dataset, "output.tsv")
    file = read_tsv_file("output.tsv")
    print(file)