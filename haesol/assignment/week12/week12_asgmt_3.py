import numpy as np
import pandas as pd


def corr(data, targets):
    target1, target2 = targets
    data_corr = data.corr()
    return round(data_corr[target1][target2], 4)
