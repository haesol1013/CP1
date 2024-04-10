def standardization(n, xi):
    for i in range(0, n+1):
        xi += i
        u = xi / n
    for j in range(0, n+1):
        r = (xi - u)**2
        r += i
        o = r/n
    xxi = (xi - u)/o**0.5

    return xxi




