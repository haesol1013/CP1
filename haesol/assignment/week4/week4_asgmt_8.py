"""""""""
# Softmax


## 설명
Softmax 함수는 입력 받은 값을 출력으로 0~1 사이의 값으로 정규화하여 출력 값들의 총합이 항상 1이 되도록 만드는 함수이다.
Softmax는 이런 특성으로 다중 클래스 분류 문제에서 마지막 레이어의 활성 함수로 자주 이용된다.
Softmax의 식은 다음과 같다.

softmax.png

3개의 입력이 들어왔을 때 각각에 대한 softmax 함수의 결과를 출력하는 프로그램을 작성해보자.
함수를 정의하되, 함수의 이름은 ‘softmax’로 고정한다. 인자를 받는 방식과 리턴하는 방식은 상관없다.

## 입력 설명
각 줄에 3개의 정수 input이 주어진다. (-100 <x<100)

## 출력 설명
첫째 줄에 3개의 input에 대한 softmax 함수 결과를 반환한다.


### 입력 예시 1 
3
6
1
### 출력 예시 1
0.04712 0.9465 0.00638

힌트
math 모듈을 이용해보자.
softmax 함수 결과는 모두 더했을 때 항상 1이 된다.
"""""""""

from math import exp


def softmax(*n: int) -> list[float]:
    list_ = list(map(exp, n))
    return [i / sum(list_) for i in list_]


if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(softmax(a, b, c))
