def sigma(n=10):
    if n > 0:
        return n + sigma(n-1)
    else:
        return 0


print(sigma())