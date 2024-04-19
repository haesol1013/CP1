"""""""""
# 팰린드롬을 아시나요?


## 설명
팰린드롬(palindrome) 또는 회문은 앞뒤를 뒤집어도 똑같은 문자열을 말한다.
ex) eye, kayak, hanna, …
주어진 문자열이 팰린드롬인지 아닌지를 검사하는 함수를 구현하고, 이를 재귀를 이용해 해결해보자.
함수 이름은 'palindrome'으로 고정한다.

## 입력 설명
첫째 줄에 test case 개수가 주어지고 두번째 줄부터 알파벳 소문자로 구성된 문자열 s가 주어진다.

## 출력 설명
각 test case마다 팰린드롬이면 1, 그렇지 않으면 0을 출력한다


### 입력 예시 1 
3
aa
abca
pallet
### 출력 예시 1
1
0
0
"""""""""


def palindrome(word: str) -> int:
    if len(word) > 1:
        if word[0] == word[-1]:
            return palindrome(word[1:-1])
        else:
            return 0
    else:
        return 1


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        input_word = input()
        print(palindrome(input_word))
