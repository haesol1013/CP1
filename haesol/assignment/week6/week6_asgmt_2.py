

def intersection(set_a: set, set_b: set) -> set:
    return set_a.intersection(set_b)


if __name__ == "__main__":
    set_a = set(input().split())
    set_b = set(input().split())
    print(intersection(set_a, set_b))
