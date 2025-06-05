"""""""""
# 소수의 합 계산

## 설명
주어진 정수 n까지의 모든 소수를 찾아 그 합을 반환하는 함수를 작성하세요. 소수를 찾는 과정에서 반복문과 조건문을 사용하고, 소수 판별을 재귀 함수로 구현하세요.
n이 2보다 작으면 "Incorrect input"을 반환하세요.
입력된 n까지의 모든 소수의 합을 계산하여 반환하세요.

## 입력 설명
정수N이 입력됩니다. (예:10,20등)
N은 소수들을 구할 범위를 의미하며, 2 이상의 자연수입니다.

## 출력 설명
N 이하의 소수들의 합을 출력합니다.


### 입력 예시 1 
10
### 출력 예시 1
17

### 입력 예시 2 
20
### 출력 예시 2
77

## 힌트
입력: 10
과정:2+3+5+7 = 17
출력: 17

입력: 20
과정:2+3+5+7+11+13+17+19 = 77
출력: 77
"""""""""

def is_prime(n, divisor=2):
    if n == divisor:
        return True

    if n % divisor == 0:
        return False
    else:
        return is_prime(n, divisor+1)


def sum_of_primes(n):
    if n < 2:
        return "Incorrect input"
    return sum(i for i in range(2, n+1) if is_prime(i))


if __name__ == "__main__":
    arg1 = int(input())
    print(sum_of_primes(arg1))