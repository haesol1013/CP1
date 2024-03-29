def palindrome(word):
    reversed_word = ''.join(reversed(word))

    if reversed_word == word:
        return 1
    else:
        return 0


T = int(input())

for i in range(T):
    input_word = input()
    result = palindrome(input_word)
    print(result)
