import matplotlib.pyplot as plt
import numpy as np

data = np.load("Covid_Decided_Count.npy")

data_str = map(str, data)
first_digit = np.array([int(x[0]) for x in data_str])
cnt = np.bincount(first_digit)[1:]

plt.bar(range(1, 10), cnt)

plt.xticks(range(1, 10))

plt.show()
