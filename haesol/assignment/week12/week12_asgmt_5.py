import numpy as np
import pandas as pd


def outlier(data):
    return data - np.mean(data) >= data.std()
