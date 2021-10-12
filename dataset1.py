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

fig, ax = plt.subplots()
x = np.linspace(-1, 1, 100)
y = true_function(x)

ax.plot(x,y)
ax.set_title("ex1.1")
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.legend("y = sin(π * x * 0.8) * 10")
plt.show()
plt.savefig("ex1.1.png")