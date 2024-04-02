def fibo(n: int) -> int:
    if n > 2:
        return fibo(n-2) + fibo(n-1)
    else:
        return n - 1


if __name__ == "__main__":
    a = int(input())
    print(fibo(a))
