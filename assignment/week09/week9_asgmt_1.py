def closer(string):
    return "Yeeun" + " " + "Alcohol" if string.startswith("Yeeun") else "Alcohol" + " " + "Yeeun"


if __name__ == "__main__":
    word = input()
    print(closer(word))
