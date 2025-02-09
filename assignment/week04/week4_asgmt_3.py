"""""""""
# 최대공약수를 구하는 함수


## 설명
20과 15의 최대공약수는 5입니다.
이름을 gcd로 하고 인자를 2개 입력받는 함수를 정의하세요.
(출력이 아닌 함수 return이어야 합니다.)

## 입력 설명
2개의 자연수 함수에 인자로 입력됩니다.
(input() 함수를 쓸 필요 없습니다.)

## 출력 설명
두 자연수의 최대공약수를 return해야 합니다.
(print() 함수를 쓸 필요 없습니다.)


### 입력 예시 1 
20 15
출력 예시 1
5

### 입력 예시 2 
36 79
### 출력 예시 2
1

### 입력 예시 3 
111 222
### 출력 예시 3
111
"""""""""


def gcd(num1: int, num2: int) -> int:
    min_num = min(num1, num2)
    for i in range(min_num, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
