

def unique(list_a: list, list_b: list) -> set:
    set_a, set_b = set(list_a), set(list_b)
    return set_a.symmetric_difference(set_b)


if __name__ == "__main__":
    list_a = input().split()
    list_b = input().split()
    print(unique(list_a, list_b))



