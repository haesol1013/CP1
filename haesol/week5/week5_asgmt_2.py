def remover(num_list: list, target: int) -> list:
    return [i for i in num_list if i != target]


def remover2(num_list: list, target: int) -> list:
    for i in num_list:
        if i == target:
            num_list.remove(target)
    return num_list


if __name__ == "__main__":
    a_list = list(map(int, input().split()))
    tgt = int(input())
    print(remover2(a_list, tgt))
