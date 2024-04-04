

def max_collatz(roster: list) -> int:
    max_list = []

    for i in roster:
        tmp = i
        cal_list = [tmp]

        while tmp != 1:
            tmp = tmp // 2 if tmp % 2 == 0 else 3*tmp + 1
            cal_list.append(tmp)

        max_list.append(max(cal_list))
        del cal_list

    return roster[max_list.index(max(max_list))]


if __name__ == "__main__":
    list_a = list(map(int, input().split()))
    print(max_collatz(list_a))
