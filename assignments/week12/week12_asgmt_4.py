import pandas as pd
import numpy as np


def max(data, target):
    return round(np.max(data[target]), 4)
