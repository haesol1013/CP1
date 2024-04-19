"""""""""
# 글자 수 세기 함수


## 설명
함수의 이름은 count로 하고 인자로 주어지는 문자열에서 특정 글자의 개수를 세는 함수를 정의하세요.
단, count 함수는 사용할 수 없습니다.

## 입력 설명
2개의 인자가 count 함수에 입력됩니다. 순서대로 탐색할 문자열, 찾아야할 문자입니다.
단, 두 번째 인자인 찾아야할 문자의 길이는 항상 1글자입니다.

## 출력 설명
문자열에서 찾은 문자의 개수를 반환합니다.


### 입력 예시 1 
examples e
### 출력 예시 1
2

### 입력 예시 2 
doyoufindfromthisword o
### 출력 예시 2
4

## 힌트
String은 Iterable의 한 종류입니다.
"""""""""


def count(word: str, target: str) -> int:
    return len([i for i in word if i == target])


def count1(word: str, target: str) -> int:
    cnt = 0
    for i in word:
        if i == target:
            cnt += 1
    return cnt


if __name__ == "__main__":
    a, b = input().split()
    print(count(a, b))
