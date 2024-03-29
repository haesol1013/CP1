string = input()
vowels = 'aeiouywAEIOUYW'

for i in range(len(string)):

    if string[i] not in vowels:
        print(string[i], end='')