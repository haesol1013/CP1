import matplotlib.pyplot as plt
import numpy as np

data = np.load("Intel_Stock_History_from_1980_03_17.npy")

data_str = map(str, data)
first_digit = [int(x[0]) for x in data_str]
cnt = np.bincount(first_digit)[1:]

plt.bar(range(1, 10), cnt)

plt.xticks(range(1, 10))

plt.show()
