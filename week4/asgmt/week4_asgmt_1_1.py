def mod(a, b):
    r = 0
    for i in range(0, b):
        d = a - i
        if d < 0:
            while d < 0:
                d += b
            if d == 0:
                r = i
        elif d > 0:
            while d > 0:
                d -= b
            if d == 0:
                r = i
        else:
            r = i
    return r