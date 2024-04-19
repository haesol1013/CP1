"""""""""
# 나머지 함수


## 설명
프로그래밍 실력이 부족하진 않았던 상준이는 남들 보다 부족하다고 생각해 매일 나머지 공부를 하고 있습니다.
상준이를 위해 나머지 값을 구해주는 함수를 만들어 보세요.
함수의 이름을 mod로 하고, 2개의 인자를 입력받아 나머지 값을 반환하는 함수를 정의하세요.
단, %(나머지) 연산자와 //(몫) 연산자는 사용할 수 없습니다.
divmod()함수도 사용할 수 없다.

## 입력 설명
정수인 2개의 인자가 함수에 입력됩니다.

## 출력 설명
입력받은 2개의 인자를 순서대로 A, B라 했을 때 A를 B로 나눈 나머지를 반환해야 합니다.


### 입력 예시 1 
3 2
### 출력 예시 1
1

### 입력 예시 2 
17 9
### 출력 예시 2
8

### 입력 예시 3 
9 3
### 출력 예시 3
0
"""""""""

import sys


def mod(num1: int, num2: int) -> int:
    opposite_sign = num1 * num2 < 0
    need_inverse = num2 < 0

    num1 = abs(num1)
    num2 = abs(num2)
    same_num = num1 == num2

    while num1 >= num2:
        num1 -= num2

    if opposite_sign and not same_num:
        num1 = num2 - num1

    if need_inverse:
        num1 *= -1

    return num1


if __name__ == "__main__":
    a, b = map(int, sys.stdin.readline().split())
    print(mod(a, b))
