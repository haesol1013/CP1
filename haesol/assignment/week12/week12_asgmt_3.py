import pandas as pd
import numpy as np


def corr(data, targets):
    target1, target2 = targets
    return round(data.corr()[target1][target2], 4)
