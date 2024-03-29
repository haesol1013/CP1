def mul5(a):
    a *= 5
    return a


def qnr(a, b=3):
    q = a // b
    r = a % b
    return q, r


def factorial(n):
    if n == 1:
        return n
    else:
        result = factorial(n-1) * n
        return result


def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

