import math


def missile(r, angle, v):
    target_theta = math.radians(angle)
    at_once = v / (r / 2)
    time = target_theta / at_once
    return time


if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(missile(a, b, c))
