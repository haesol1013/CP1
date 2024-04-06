

def max_collatz(roster: list) -> int:
    max_list = []

    for i in roster:
        cal_list = [i]

        while i != 1:
            i = i // 2 if i % 2 == 0 else 3 * i + 1
            cal_list.append(i)

        max_list.append(max(cal_list))
        del cal_list

    return roster[max_list.index(max(max_list))]


if __name__ == "__main__":
    list_a = list(map(int, input().split()))
    print(max_collatz(list_a))
