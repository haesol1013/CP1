import pandas as pd
import numpy as np


def sinmax(data):
    return data.apply(np.sin).apply(np.max, axis=1)
