"""""""""
# 콜라츠 최대값(Collatz Maxima)


## 설명
1937년 로타르 콜라츠(Lothar Collatz)가 제기한 추측으로, 다음의 과정을 거치면 모든 수는 결국 1이 될 것이라는 추측입니다
임의의 수n이 홀수라면, 3을 곱한 후 1을 더합니다.
만약 짝수라면, 2로 나눕니다.

collatz.png

이 과정을 나오는 결과값에 반복하여 적용하면 결국 모든 수는 1이 될 것입니다.
이 과정에서 발생하는 수열을 콜라츠 수열(Collatz sequence)이라고 합니다.
콜라츠 수열은 크게 진동하다가 점점 안정되는 형태를 띄는데, 진동에 의해 발생한 가장 큰 값을 콜라츠 최대값(Collatz Maxima)라고 합니다.

예를 들어, 7의 콜라츠 수열은 7 - 22 - 11 - 34 - 17 - 52 - 26 - 13 - 40 - 20 - 10 - 5 - 16 - 8 - 4 - 2 - 1 이 됩니다. 
여기서 콜라츠 최대값은 52입니다.
3의 콜라츠 수열은 3 - 10 - 5 - 16 - 8 - 4 - 2 - 1 이 됩니다. 여기서 콜라츠 최대값은 16입니다.

함수의 이름을 max_collatz로 하고, 어떤 수들이 List 타입으로 주어질 때 콜라츠 최대값이 가장 큰 값n을 반환하는 함수를 정의하세요.


## 입력 설명
Integer타입 자연수들이 List로 주어집니다.

## 출력 설명
주어진 List 중 콜라츠 최대값이 가장 큰 값 하나를 콜라츠 최대값이 아닌 '원래 값'으로 반환합니다.


### 입력 예시 1 
[5, 7, 13]
### 출력 예시 1
7

### 입력 예시 2 
[5, 7, 13, 50]
### 출력 예시 2
50

### 입력 예시 3 
[2, 3, 4]
### 출력 예시 3
3
"""""""""


def max_collatz(roster: list[int]) -> int:
    max_list = []

    for n in roster:
        cal = [n]

        while n != 1:
            n = n//2 if n % 2 == 0 else n*3 + 1
            cal.append(n)

        max_list.append(max(cal))
        del cal

    return roster[max_list.index(max(max_list))]


if __name__ == "__main__":
    list_a = list(map(int, input().split()))
    print(max_collatz(list_a))
