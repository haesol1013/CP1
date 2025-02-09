"""""""""
# Strong Integer


## 설명
Python에서는 정수와 실수의 덧셈 또는 뺄셈이 실행되면, 더 많은 범위의 수를 구현할 수 있는 실수로 자동으로 변환되어 계산됩니다.
예를 들어 3+1.7을 실행하면, 정수인 3이 실수인 3.0으로 변환된 후 계산되어 4.7이 됩니다.

정수를 끔찍히 사랑하는 강정수(Strong Integer) 선배는 이런 변환 과정이 탐탁치 않았습니다.
강정수 선배를 위해 정수가 실수로 변환되어 계산되는 것이 아닌, 실수가 정수로 변환되어 계산되는 클래스를 정의하세요.
Class의 이름은 integer로 하고 + 또는 - 연산을 실행할 때 정수로 변환해 계산하는 Class를 정의하세요.

## 조건
1. Object로 생성될 때, 하나의 값을 인자로 받아 정수로 변환해 속성(내부 변수)에 저장한다.
2. Object에 + 연산이 발생할 경우, 생성시 저장된 속성 값에 연산되는 값을 정수로 변환해 덧셈한 후 반환한다.
3.Object에 - 연산이 발생할 경우,생성시 저장된 속성 값에연산되는 값을 정수로 변환해 뺄셈한 후 반환한다.

## 입력 설명
하나의 실수가 클래스 인자로 입력되고, 임의의 실수가 + 또는 - 연산에 사용됩니다.

## 출력 설명
생성 인자로 입력 받은 값을 정수로 저장하고, + 또는 -에 대한 연산이 실행되면 정수로 변환하여 계산한 값을 반환해야 합니다.


### 입력 예시 1 
i=integer(10)
i+3.7
i-1.9
### 출력 예시 1
13
9

### 입력 예시 2 
i=integer(1.5)
i+1.7
i-0.1
### 출력 예시 2
2
1
"""""""""


class integer:
    def __init__(self, val: float) -> None:
        self.val = int(val)

    def __add__(self, other: float) -> int:
        return self.val + int(other)

    def __sub__(self, other: float) -> int:
        return self.val - int(other)


if __name__ == "__main__":
    num_a = integer(float(input()))
    num_b = float(input())
    num_c = float(input())

    print(num_a + num_b)
    print(num_a - num_c)