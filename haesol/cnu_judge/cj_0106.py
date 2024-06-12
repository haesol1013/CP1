"""""""""
# [기말-06]콜라츠 최대값(Collatz Maxima)


## 설명
1937년 로타르 콜라츠(Lothar Collatz)가 제기한 추측으로, 다음의 과정을 거치면 모든 수는 결국 1이 될 것이라는 추측입니다.
임의의 수image.png이 홀수라면, 3을 곱한 후 1을 더합니다.
만약 짝수라면, 2로 나눕니다.

이 과정을 나오는 결과값에 반복하여 적용하면 결국 모든 수는 1이 될 것입니다.
이 과정에서 발생하는 수열을 콜라츠 수열(Collatz sequence)이라고 합니다.
콜라츠 수열은 크게 진동하다가 점점 안정되는 형태를 띄는데, 진동에 의해 발생한 가장 큰 값을 콜라츠 최대값(Collatz Maxima)라고 합니다.
예를 들어, 7의 콜라츠 수열은 7 - 22 - 11 - 34 - 17 - 52 - 26 - 13 - 40 - 20 - 10 - 5 - 16 - 8 - 4 - 2 - 1 이 됩니다. 여기서 콜라츠 최대값은 52, 그 다음 큰 값은 40입니다.
3의 콜라츠 수열은 3 - 10 - 5 - 16 - 8 - 4 - 2 - 1 이 됩니다. 여기서 콜라츠 최대값은 16, 그 다음 큰 값은 10입니다.
함수의 이름을 collatz로 하고, 어떤 수가int 타입으로 주어질 때 콜라츠 최대값이 가장 큰 값과 그 다음 큰 값의 차를반환하는 함수를 정의하세요.

허용 라이브러리 : math, numpy

## 입력 설명
Integer타입 자연수가 주어집니다.

## 출력 설명
콜라츠 최대값과 그 다음 큰 값의 차를 반환합니다.


### 입력 예시 1 
7
### 출력 예시 1
12

### 입력 예시 2 
3
### 출력 예시 2
6

### 입력 예시 3 
13
### 출력 예시 3
20
"""""""""


def collatz(num: int):
    sequence = [num]
    while num != 1:
        num = num // 2 if num % 2 == 0 else num*3 + 1
        sequence.append(num)
    n1, n2 = sorted(set(sequence))[-2:]
    return n2 - n1


if __name__ == "__main__":
    arg = int(input())
    print(collatz(arg))

