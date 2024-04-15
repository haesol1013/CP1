

def concat(pre_tuple: tuple, post_tuple: tuple) -> tuple:
    return pre_tuple + post_tuple


if __name__ == "__main__":
    tuple_a = tuple(map(int, input().split()))
    tuple_b = tuple(map(int, input().split()))
    print(concat(tuple_a, tuple_b))
