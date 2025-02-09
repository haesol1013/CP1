a = input()
b = input()
merge = [a, b]
result = "Ascending" if merge == sorted(merge) else "Descending"
print(result)
