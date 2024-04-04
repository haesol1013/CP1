def concat(num1: int, num2: int) -> list:
    return [num1, num2]


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(concat(a, b))
