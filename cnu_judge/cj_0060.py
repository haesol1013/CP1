def max_collatz(roster: list) -> int:
    max_list = []
    for i in roster:
        max_num = 0
        while i > 1:
            i = i // 2 if i % 2 == 0 else i * 3 + 1
            if i > max_num:
                max_num = i
        max_list.append(max_num)
    return roster[max_list.index(max(max_list))]


if __name__ == "__main__":
    list_ = list(map(int, input().split()))
    print(max_collatz(list_))