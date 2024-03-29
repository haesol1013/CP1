import math
import random

x = int(input())
y = int(input())

avg1 = random.randint(-4, 4)
avg2 = random.randint(-4, 4)
std1 = random.randrange(1, 5)
std2 = random.randrange(1, 5)

PI = math.pi
Z = (math.exp(-((x - avg1) / (2 * std1**2))) / (2 * PI * std1**2)**0.5 *
math.exp(-((y - avg2) / (2 * std2**2))) / (2 * PI * std2**2)**0.5)

print(Z)