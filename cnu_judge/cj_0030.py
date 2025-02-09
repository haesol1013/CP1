def intersection(set_1: set, set_2: set) -> set:
    return set_1.intersection(set_2)


if __name__ == "__main__":
    a = set(input().split())
    b = set(input().split())
    print(intersection(a, b))
