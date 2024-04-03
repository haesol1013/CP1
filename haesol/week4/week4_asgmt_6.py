def add(num1: int, num2: int) -> int:
    return num1 + num2


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(add(a, b))
