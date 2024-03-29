def palindrome(word, cnt, reversed_word=''):
    if cnt > -1:
        reversed_word = word[cnt]
        return reversed_word + palindrome(word=word, cnt=cnt-1)
    else:
        return reversed_word


T = int(input())

for i in range(T):
    input_word = input()
    len_ = len(input_word)
    print(palindrome(input_word, len_-1))
