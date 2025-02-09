import matplotlib.pyplot as plt
import numpy as np

data = np.load("Covid_Decided_Count.npy")

str_data = map(str, data)
first_digit = [int(x[0]) for x in str_data]
cnt = np.bincount(first_digit)[1:]

# plt.bar(range(1, 10), cnt)
#
# plt.xticks(range(1, 10))
#
# plt.show()


plt.pie(cnt, labels=list(map(str, range(1, 10))), autopct="%.3f")
plt.show()
