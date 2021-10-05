import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib #日本語対応

def true_function(x):
    """
    >>> true_function(0)
    0
    """
    y = np.sin(np.pi * x * 0.8) * 10
    return y

x = np.arange(-1,1,0.01)
graph = true_function(x)

plt.plot(graph)
plt.title("ex1.1")
plt.xlabel("x")
plt.ylabel("y")
plt.legend("y = sin(π * x * 0.8) * 10")
plt.show()
plt.savefig("ex1.1.png")