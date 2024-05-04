def palindrome(word: str, cnt: int = 1) -> int:
    if cnt == 1:
        word = word.replace(' ', '')

    if len(word) > 1:
        if word[0] == word[-1]:
            return palindrome(word[1:-1], cnt+1)
        else:
            return cnt

    return cnt


if __name__ == "__main__":
    word = input()
    print(palindrome(word))