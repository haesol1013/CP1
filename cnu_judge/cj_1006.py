n = int(input())
sequence = [0, 1, 1] + [0 for _ in range(n - 2)]

for i in range(3, n + 1):
    sequence[i] = sequence[i - 2] + sequence[i - 1]

print(sequence[n])
