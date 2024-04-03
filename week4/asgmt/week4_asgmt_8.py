from math import exp


def softmax(num1: int, num2: int, num3: int) -> tuple:
    exp_num1, exp_num2, exp_num3 = exp(num1), exp(num2), exp(num3)

    sigma = exp_num1 + exp_num2 + exp_num3
    a_r = exp_num1 / sigma
    b_r = exp_num2 / sigma
    c_r = exp_num3 / sigma
    return a_r, b_r, c_r


if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(softmax(a, b, c))
