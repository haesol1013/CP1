def norm(lst):
    result = 0
    for i in lst:
        result += i**2
    result **= 0.5
    return round(result, 2)
