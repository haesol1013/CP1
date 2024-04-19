"""""""""
# 덧셈 함수


## 설명
함수의 이름을 add로 하고 2개의 인자를 덧셈하여 반환하는 함수를 정의하세요.

## 입력 설명
2개의 정수 인자가 add 함수에 입력됩니다.

## 출력 설명
두 인자를 덧셈하여 반환하세요.

### 입력 예시 1 
5 9
### 출력 예시 1
14

### 입력 예시 2 
-1 1
### 출력 예시 2
0
"""""""""


def add(num1: int, num2: int) -> int:
    return num1 + num2


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(add(a, b))
