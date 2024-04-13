def unique(list_1: list, list_2: list) -> set:
    return set(list_1).symmetric_difference(set(list_2))


if __name__ == "__main__":
    a = input().split()
    b = input().split()
    print(unique(a, b))