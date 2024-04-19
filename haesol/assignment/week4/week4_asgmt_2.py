"""""""""
# 제곱 함수


## 설명
함수의 이름은 power로 하고, 지수는 기본값으로 2로 하여 인자가 1개만 주어지면 2제곱하여 반환하고, 인자가 2개 주어지면 N제곱하여 반환하는 함수를 정의하세요.
단, **(Double Asterisk) 연산은 사용할 수 없으며 for 또는 while문을 이용해 구현해야 합니다.

## 입력 설명
1개 또는 2개의 정수가 주어집니다. 순서대로 밑, 지수가 인자로 입력됩니다.
(input이 아닌 def으로 함수 정의)

## 출력 설명
주어진 입력에 대해 제곱하여 반환합니다.
(print가 아닌 return으로 반환)


### 입력 예시 1 
3
### 출력 예시 1
9

### 입력 예시 2 
2 4
### 출력 예시 2
16

### 입력 예시 3 
135935 0
### 출력 예시 3
1
"""""""""


def power(base: int, exponent: int = 2) -> float:
    result = 1

    if exponent >= 0:
        for i in range(exponent):
            result = result * base
    else:
        for i in range(exponent, 0):
            result = result / base

    return result


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(power(a, b))
