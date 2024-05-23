import pandas as pd
import numpy as np


def sinmax(data):
    data_sin = data.apply(np.sin)
    return data_sin.apply(np.max, axis=1)
