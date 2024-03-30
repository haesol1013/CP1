def mod(m, n):
    if m > 0:
        while m > 0:
            m -= n
        if m == 0:
            return m
        else:
            return m + n

    elif m < 0:
        while m < 0:
            m += n
        return m

    else:
        return m


a, b = map(int, input().split())
print(mod(a, b))
print(a % b)