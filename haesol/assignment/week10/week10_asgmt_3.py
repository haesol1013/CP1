import numpy as np


def outlier(arr):
    return arr - np.mean(arr) >= arr.std()


if __name__ == "__main__":
    arr = np.array([0.5, 0.3, 0.1, 0.2, 10.0])
    print(outlier(arr))
