def fibo(n):
    if n <= 2:
        return n-1
    elif n > 2:
        return fibo(n-2) + fibo(n-1)