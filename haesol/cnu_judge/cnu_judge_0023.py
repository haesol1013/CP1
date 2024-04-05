import sys


def qnr(num1: int, num2: int) -> tuple:
    opposite_sign = num1 * num2 < 0
    need_inverse = num2 < 0
    quotient = 0

    num1 = abs(num1)
    num2 = abs(num2)
    same_num = num1 == num2

    while num1 >= num2:
        num1 -= num2
        quotient += 1

    if opposite_sign:
        if not same_num:
            num1 = num2 - num1
            quotient += 1
        quotient *= -1

    if need_inverse:
        num1 *= -1

    return quotient, num1


if __name__ == "__main__":
    a, b = map(int, sys.stdin.readline().split())
    print(qnr(a, b))
    print((a // b, a % b))