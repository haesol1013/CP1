def power(base, exponent=2):
    result = 1

    if exponent >= 0:
        for i in range(exponent):
            result = result * base
    else:
        for i in range(exponent, -1):
            result = result * (1 / base)

    return result


print(power(2, 0.5))
