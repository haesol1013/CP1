import math


def softmax(a: int, b: int, c: int) -> tuple:
    sigma = math.exp(a) + math.exp(b) + math.exp(c)
    a_r = math.exp(a) / sigma
    b_r = math.exp(b) / sigma
    c_r = math.exp(c) / sigma
    return a_r, b_r, c_r


if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(softmax(a, b, c))
