

def unique(list_a: list, list_b: list) -> set:
    return set(list_a).symmetric_difference(set(list_b))


if __name__ == "__main__":
    list_a = input().split()
    list_b = input().split()
    print(unique(list_a, list_b))



