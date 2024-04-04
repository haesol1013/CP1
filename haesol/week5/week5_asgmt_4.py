def norm(num_list: list) -> float:
    square_list = [i**2 for i in num_list]
    hap = 0
    for i in square_list:
        hap += i
    return round(hap**0.5, 2)


def norm2(num_list: list) -> float:
    result = 0
    for i in num_list:
        result += i**2
    return round(result**0.5, 2)


if __name__ == "__main__":
    list_a = map(int, input().split())
    print(norm2(list_a))
