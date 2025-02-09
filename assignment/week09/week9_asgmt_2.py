def find_socks(words: str) -> str:
    arr = words.split()
    arr.remove("Socks")
    arr.insert(0, "Socks")
    return ' '.join(arr)


if __name__ == "__main__":
    words = input()
    print(find_socks(words))
