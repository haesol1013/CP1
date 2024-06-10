# 중앙 차분

class Differential(Function):
    def get(self, x):
        h = 0.00000001
        return (super().get(x+h) - super().get(x-h)) / (2*h)