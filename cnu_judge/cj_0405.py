# [기말-05]수치 적분

import numpy as np


class Function:
    def __init__(self, func: str):
        self.connective_operator = func[3]
        self.coefficient = int(func[2])

    def get(self, x):
        return x * self.coefficient


class Integral(Function):
    def get(self, a, b, h):
        result = 0
        for x in np.arange(a, b, h):
            result += (x+h - x) * (super().get(x) + super().get(x+h)) / 2
        return result


if __name__ == "__main__":
    f = Integral("y=2*x")
    r = f.get(0, 3, 1)
    print(r)