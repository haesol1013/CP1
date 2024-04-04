list_a = input().split()
list_b = input().split()
result = []

for i in range(len(list_a)):
    result.append(list_a[i])
    result.append(list_b[i])

print(*result)
# print(' '.join(result))
