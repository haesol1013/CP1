import numpy as np
import pandas as pd


def corr(data, targets):
    target1, target2 = targets
    return round(data.corr()[target1][target2], 4)
