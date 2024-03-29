import math


def softmax(a, b, c):
    sigma = math.exp(a) + math.exp(b) + math.exp(c)
    a_r = math.exp(a) / sigma
    b_r = math.exp(b) / sigma
    c_r = math.exp(c) / sigma
    return a_r, b_r, c_r
