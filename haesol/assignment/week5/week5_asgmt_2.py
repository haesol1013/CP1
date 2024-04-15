

def remover(num_list: list, target: int) -> list:
    return [i for i in num_list if i != target]


def remover1(num_list: list, target: int) -> list:
    cnt = 0
    for i in num_list:
        if i == target:
            cnt += 1
    for i in range(cnt):
        num_list.remove(target)
    return num_list


def remover2(num_list: list, target: int) -> list:
    cnt = num_list.count(target)
    for i in range(cnt):
        num_list.remove(target)
    return num_list


def remover3(num_list: list, target: int) -> list:
    while True:
        try:
            num_list.remove(target)
        except ValueError:
            break
    return num_list


if __name__ == "__main__":
    list_ = list(map(int, input().split()))
    tgt = int(input())
    print(remover(list_, tgt))
