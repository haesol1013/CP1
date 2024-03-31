def palindrome(word):
    if len(word) > 1:
        if word[0] == word[-1]:
            return palindrome(word[1:-1])
        else:
            return 0
    else:
        return 1


t = int(input())
for i in range(t):
    input_word = input()
    print(palindrome(input_word))
