num1 = int(input())
a = num1 // 1000
b = num1 % 1000 // 100
c = num1 % 1000 % 100 // 10
d = num1 % 1000 % 100 % 10

list1 = [a, b, c, d]
for i in list1:
    print(i)