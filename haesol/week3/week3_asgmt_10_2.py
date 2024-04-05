n = int(input())
cnt = 0

for i in range(2, n+1):
    divisor_list = [j for j in range(2, i+1) if i % j == 0]
    if len(divisor_list) == 1:
        cnt += 1

print(cnt)
