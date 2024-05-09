import numpy as np


def box(arr):
    return round(np.sum(np.pi * (4/3) * arr**3), 4)


if __name__ == "__main__":
    print(box(np.array([1, 1, 1, 1, 1])))
