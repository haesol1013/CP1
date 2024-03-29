N = int(input())
result = 0
i = 0

while N != 0:
    remainder = N % 2
    N //= 2
    result += remainder * 10**i
    i += 1

print(result)
