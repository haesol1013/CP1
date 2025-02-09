def triangular_walk(walk: int) -> tuple:
    i = 2
    num = [1]
    while num[-1] < walk:
        num.append(num[-1] + i)
        i += 1

    pos = [0, 1]
    pos_list = []
    up = True

    for i in range(0, len(num)):
        if up:
            pos[0] += 1
            pos_list.append(tuple(pos))
            for j in range(0, i):
                pos[0] -= 1
                pos[1] += 1
                pos_list.append(tuple(pos))
            up = False
        else:
            pos[1] += 1
            pos_list.append(tuple(pos))
            for j in range(0, i):
                pos[0] += 1
                pos[1] -= 1
                pos_list.append(tuple(pos))
            up = True

    return pos_list[walk-1]


if __name__ == "__main__":
    n = int(input())
    print(triangular_walk(n))
