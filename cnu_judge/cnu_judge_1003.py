days = int(input())
years = days // 365
years += 1900
result = (years % 4 == 0 and years % 100 != 0) or years % 400 == 0
print(result)
