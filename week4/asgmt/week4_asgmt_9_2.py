def palindrome(a, i=0):
    if i < 3:
        i += 1
        return palindrome(a, i)
    else:
        return a

print(palindrome('a'))

