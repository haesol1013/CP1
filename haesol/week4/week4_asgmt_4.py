def count(string: str, target: str) -> int:
    cnt = 0

    for i in string:
        if target == i:
            cnt += 1

    return cnt


def count1(string: str, target: str) -> int:
    return len([i for i in string if i == target])


def count2(string: str, target: str) -> int:
    return len(string) - len(string.replace(target, ''))


if __name__ == "__main__":
    a, b = input().split()
    print(count(a, b))
