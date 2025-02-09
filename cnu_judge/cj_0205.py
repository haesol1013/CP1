# 고기 잡이
import numpy as np


def fisherman(arr, n):
    catchable_fishes = []
    arr = np.array(arr)
    for fish in arr:
        x, y = fish
        cond = (x <= arr[:,0]) & (x+n >= arr[:,0]) & (y <= arr[:,1]) & (y+n >= arr[:,1])
        catchable_fish = arr[cond].shape[0]
        catchable_fishes.append(catchable_fish)
    return max(catchable_fishes)


if __name__ == "__main__":
    arg = [[ 1, 1],
           [ 2, 4],
           [ 1, 9],
           [ 7, 3],
           [ 6, 7],
           [ 8, 8],
           [ 7, 9]]
    arg = np.array(arg)
    print(fisherman(arg, 5))
