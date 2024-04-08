def remover(a, b):
    L = [i for i in a if i != b]
    return L


print(remover([1, 2, 3], 1))
