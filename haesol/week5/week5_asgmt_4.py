

def norm(num_list: list) -> float:
    result = 0
    for i in num_list:
        result += i**2
    return round(result**0.5, 2)


def norm1(num_list: list) -> float:
    square_list = [i**2 for i in num_list]
    result = 0
    for i in square_list:
        result += i
    return round(result**0.5, 2)


if __name__ == "__main__":
    list_a = list(map(int, input().split()))
    print(norm1(list_a))
