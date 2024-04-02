def gcd(num1: int, num2: int) -> int:
    cd = 1
    for i in range(2, min(num1, num2) + 1)[::1]:
        if num1 % i == 0 and num2 % i == 0:
            cd = i

    return cd


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
