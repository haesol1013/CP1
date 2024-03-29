def count(string, char_):
    cnt = 0
    
    for i in string:
        if char_ == i:
            cnt += 1

    return cnt
