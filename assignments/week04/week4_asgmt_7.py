"""""""""
# Fibonacci


## 설명
함수 이름을 fibo로 하고, N번째 피보나치 수열이 무엇인 지 반환하는 함수를 Recursion을 활용해 정의하세요.
(단, 1번째는 0이 됩니다.)
e.g. [0, 1, 1 ,2 ,3 ,5, 8, ... ] , N=1>>0

## 입력 설명
1개의 자연수가 함수 인자로 입력됩니다.

## 출력 설명
N번째 피보나치 수를 반환합니다.


### 입력 예시 1 
1
### 출력 예시 1
0

### 입력 예시 2 
5
### 출력 예시 2
3

### 입력 예시 3 
10
### 출력 예시 3
34
"""""""""


def fibo(n: int) -> int:
    if n > 2:
        return fibo(n-1) + fibo(n-2)
    else:
        return n - 1


if __name__ == "__main__":
    a = int(input())
    print(fibo(a))
