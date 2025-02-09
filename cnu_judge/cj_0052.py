def divergence(a0: float, a1: float, n: float) -> float:
    n = int(n)
    if n == 0:
        return a0
    elif n == 1:
        return a1
    else:
        return divergence(a0, a1, n-2) / divergence(a0, a1, n-1)


if __name__ == "__main__":
    a0, a1, n = map(float, input().split())
    print(divergence(a0, a1, n))
