import math
distance, timelimit = [int(i) for i in input().split()]

n = int(input())

for i in range(n):
    shape, radius, rpm = input().split()
    shape = int(shape)
    radius = float(radius)
    rpm = float(rpm)

    if shape == 0:
        perimeter = 2 * radius * math.pi
    else:
        perimeter = 2 * radius * math.sin(math.radians(180/shape)) * shape

    result = perimeter * rpm * (timelimit / 60) >= distance
    print(result)
