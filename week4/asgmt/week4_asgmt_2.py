def power(base: int, exponent: int = 2) -> float:
    result = 1

    if exponent >= 0:
        for i in range(exponent):
            result = result * base
    else:
        for i in range(exponent, 0):
            result = result / base

    return result


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(power(a, b))
