"""""""""
# [40점] 콜라츠 추측(Collatz Conjecture)

## 설명
1937년 로타르 콜라츠(Lothar Collatz)가 제기한 추측으로, 다음의 과정을 거치면 모든 수는 결국 1이 될 것이라는 추측입니다.

임의의 수image.png이 홀수라면, 3을 곱한 후 1을 더합니다.

만약 짝수라면, 2로 나눕니다.

이 과정을 나오는 결과값에 반복하여 적용하면 결국 모든 수는 1이 될 것입니다.
이 과정에서 발생하는 수열을 콜라츠 수열(Collatz sequence)이라고 합니다.

예를 들어, 7의 콜라츠 수열은 7 - 22 - 11 - 34 - 17 - 52 - 26 - 13 - 40 - 20 - 10 - 5 - 16 - 8 - 4 - 2 - 1 이 됩니다.
3의 콜라츠 수열은 3 - 10 - 5 - 16 - 8 - 4 - 2 - 1 이 됩니다.

함수의 이름을 collatz로 하고, 어떤 수image.png이 주어질 때 콜라츠 수열을 Iterable 타입(List, Tuple 등)으로 반환하는 함수를 정의하세요.

허용 라이브러리 : math, numpy

## 입력 설명
하나의 Integer 타입 자연수가 주어집니다.

## 출력 설명
콜라츠 수열을 Iterable(List, Tuple 등) 타입으로 반환해야 합니다.


### 입력 예시 1 
7
### 출력 예시 1
[7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1]

### 입력 예시 2 
3
### 출력 예시 2
[3,10,5,16,8,4,2,1]
"""""""""

def collatz(num: int):
    sequence = [num]
    while num != 1:
        num = num // 2 if num % 2 == 0 else num*3 + 1
        sequence.append(num)
    return sequence


if __name__ == "__main__":
    arg = int(input())
    print(collatz(arg))
