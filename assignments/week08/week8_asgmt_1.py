"""""""""
# Assertion


## 설명
다음 코드는 두 값을 인자로 받아 나머지를 계산해 반환하는 함수를 목표로 작성한 코드입니다.
b가 0인 경우 0으로 나누게 되므로 계산할 수 없는 로직이 됩니다.
assert 명령을 이용해 0으로 나누는 상황이 발생할 경우 "Don't divide by 0" 라고 출력하는 함수를 완성하세요.

## 입력 설명
나누어지는 값 a, 나누는 값 b가 함수 인자로 입력됩니다.

## 출력 설명
a가 0으로 나누어지는 경우 Don't divide by 0 를 출력하고, 정상적으로 나누어지는 경우 나머지 값이 출력해야 합니다.


### 입력 예시 1 
1 1
### 출력 예시 1
0

### 입력 예시 2 
15 0
### 출력 예시 2
AssertionError: Don't divide by 0
"""""""""


def remainder(a, b):
    assert b != 0, "Don't divide by 0"
    return a % b



print(remainder(15, 1))
