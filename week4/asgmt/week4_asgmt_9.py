def palindrome(word):
    if len(word) > 1:
        if word[0] == word[-1]:
            return palindrome(word[1:-1])
        else:
            return 0
    else:
        return 1


T = int(input())
for i in range(T):
    input_word = input()
    print(palindrome(input_word))
