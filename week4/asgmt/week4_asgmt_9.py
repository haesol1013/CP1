def palindrome(word, repeat=0):
    if repeat == 0:
        return palindrome(word, 1)
    else:
        reversed_word = ''.join(reversed(word))
        if reversed_word == word:
            return 1
        else:
            return 0


T = int(input())

for i in range(T):
    input_word = input()
    print(palindrome(input_word))