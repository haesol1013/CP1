N = int(input())
count_prime = 0

for i in range(2, N+1):
    count_divisor = 0

    for j in range(2, i+1):
        if i % j == 0:
            count_divisor += 1

    if count_divisor == 1:
        count_prime += 1

print(count_prime)