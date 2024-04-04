a = input().split()
b = input().split()
result = []

for i in range(len(a)):
    result.append(a[i])
    result.append(b[i])

print(' '.join(result))
