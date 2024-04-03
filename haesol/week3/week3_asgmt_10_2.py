N = int(input())
def is_prime(number):
    return not any(number % i == 0 for i in range(2, int(number ** 0.5) + 1))

count = 0
for i in range(2, N+1):
    if is_prime(i):
        count += 1

print(count)
