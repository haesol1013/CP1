

def standardization(list_x: list) -> list:
    mu = sum(list_x) / len(list_x)
    std = sum([(x-mu)**2 for x in list_x]) / len(list_x)
    return [(x-mu) / std**0.5 for x in list_x]


if __name__ == "__main__":
    list_a = list(map(int, input().split()))
    print(standardization(list_a))
