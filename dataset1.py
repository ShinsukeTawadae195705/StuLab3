import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib #日本語対応
import random
import pandas as pd

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

""" #描画
fig, ax = plt.subplots()
x = np.linspace(-1, 1, 100)
y = true_function(x)

ax.plot(x,y)
ax.set_title("ex1.1")
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.legend("y = sin(π * x * 0.8) * 10")
plt.show()
plt.savefig("ex1.1.png") """

"""
演習1.2
"""
#先にex1.1の図を描画
fig, ax = plt.subplots()
x = np.linspace(-1, 1, 100)
y = true_function(x)
ax.plot(x,y)

random.seed(20)
x = [random.uniform(-1,1) for _ in range(20)] #-1<=x<=1の範囲の乱数を20個生成
y = [true_function(i) for i in x]
df = pd.DataFrame({"観測点": x, "真値": y})
#print(df)

""" ax.set_title("ex1.2")
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.legend("y = sin(π * x * 0.8) * 10")
plt.scatter(x,y)
plt.show()
plt.savefig("ex1.2.png") """

"""
演習1.3
"""
noizes = [np.random.normal(0, 2) for _ in range(20)] #平均0, 標準偏差2のノイズを生成
#print(noizes)
noizes = [i/2 for i in noizes]
#print(noizes)
y = [i+noizes[num] for num,i in enumerate(y)]
noizes_df = pd.DataFrame({"観測値": y})
df = pd.concat([df, noizes_df], axis=1)
#print(df)

#描画
fig, ax = plt.subplots()
x = np.linspace(-1, 1, 100)
y = true_function(x)
ax.plot(x,y, label="y = sin(π * x * 0.8) * 10")

random.seed(20)
x = [random.uniform(-1,1) for _ in range(20)] #-1<=x<=1の範囲の乱数を20個生成
y = [true_function(i) for i in x]
df = pd.DataFrame({"観測点": x, "真値": y})
#print(df)

ax.set_title("ex1.3")
ax.set_xlabel("x")
ax.set_ylabel("y")
#plt.legend("y = sin(π * x * 0.8) * 10")
plt.scatter(x,y)
plt.scatter(x, noizes, label="noizes")
plt.legend()
plt.show()
plt.savefig("ex1.3.png")