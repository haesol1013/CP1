"""""""""
# [70점] 욕망의 항아리

## 설명
욕망의 항아리에는 N장의 숫자 카드들이 들어있습니다.
N장을 모두 꺼내고, 꺼낸 순서대로 순열을 만듭니다.
이 항아리에 카드가 많이 들어있을수록 소수가 되는 경우의 수는 점점 줄어들게 됩니다.
욕심부리지 않고 카드를 적정량만 보관해야한다는 것을 보여주기 위해, 항아리에 들어있는 카드들로만들 수 있는 순열들 중 소수가 되는 경우의 수를 구하세요.
함수의 이름은 desire으로 합니다.

허용 라이브러리: 없음

## 입력 설명
첫 번째 인자로 N장의 숫자 카드가 1차원 리스트로 입력됩니다.

## 출력 설명
카드를 모두 꺼내 만든 순열이 소수인 경우의 수를 Integer로 반환합니다.
(단, 같은 숫자가 적힌 카드더라도 서로 다른 카드이므로 중복이 허용됩니다.)


### 입력 예시 1 
[1, 2, 3, 4]
출력 예시 1
4

### 입력 예시 2 
[1, 1]
### 출력 예시 2
2

### 입력 예시 3 
[2, 3]
### 출력 예시 3
1

### 입력 예시 4 
[0, 0, 3, 7]
### 출력 예시 4
6

### 입력 예시 5 
[1,2,3,4,5,6,7,8,9]
### 출력 예시 5
0
"""""""""


def desire(data):
    cnt = 0
    def _backtrack_perms(curr, remain):
        if not remain:
            val = sum(i * 10**exp for exp, i in enumerate(curr))
            if is_prime(val):
                nonlocal cnt
                cnt += 1
        for i, v in enumerate(remain):
            new_remain = remain[:i] + remain[i+1:]
            _backtrack_perms(curr+[v], new_remain)
    _backtrack_perms([], data)
    return cnt


def is_prime(n: int) -> int:
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    arg1 = list(map(int, input().split()))
    print(desire(arg1))