import pandas as pd
import numpy as np


def outlier(data):
    return data - np.mean(data) >= data.std()
