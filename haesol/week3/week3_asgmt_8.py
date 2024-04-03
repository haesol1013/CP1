str_ = input()
vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'w',
          'A', 'E', 'I', 'O', 'U', 'Y', 'W']

for i in range(len(str_)):
    if str_[i] not in vowels:
        print(str_[i], end='')
