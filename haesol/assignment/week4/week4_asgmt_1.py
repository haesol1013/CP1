import sys


def mod(num1: int, num2: int) -> int:
    opposite_sign = num1 * num2 < 0
    need_inverse = num2 < 0

    num1 = abs(num1)
    num2 = abs(num2)
    same_num = num1 == num2

    while num1 >= num2:
        num1 -= num2

    if opposite_sign and not same_num:
        num1 = num2 - num1

    if need_inverse:
        num1 *= -1

    return num1


if __name__ == "__main__":
    a, b = map(int, sys.stdin.readline().split())
    print(mod(a, b))
