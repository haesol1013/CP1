"""""""""
# 원소 제거기


## 설명
함수의 이름을 remover로 하고, 2개의 인자를 입력받아 리스트의 특정 원소들을 모두 제거하여 반환하는 함수를 정의하세요.

## 입력 설명
2개의 인자가 입력되며 첫 번째 인자는 List, 두 번째 인자는 제거할 값입니다.
e.g. [1, 2, 3] 과 1

## 출력 설명
List인 첫 번째 인자에서 두 번째 인자의 값을 모두 제거한 List를 출력해야 합니다.
e.g. [2, 3]


### 입력 예시 1 
1 2 3
1
### 출력 예시 1
[2, 3]

### 입력 예시 2 
0 1 1 2 3 5 8
1
### 출력 예시 2
[0, 2, 3, 5, 8]

힌트
remove 함수를 끝까지 사용하면 에러가 발생한다. 제거할 원소가 없음에도 remove 명령이 실행됐기 때문이다.

Basic Hint 1 ) for문을 이용해 제거할 원소가 몇 개가 존재하는 지 알 수 있다.
Basic Hint 2 ) count함수를 이용해 특정 값의 개수를 확인할 수 있다.
Advanced Hint ) Try ~ Except 문을 이용할 수 있다. 
                구글에 ' python try except ' 로 검색하면 사용법을 찾아볼 수 있다.
"""""""""


def remover(obj: list, target: int) -> list:
    return [i for i in obj if i != target]


def remover1(obj: list, target: int) -> list:
    cnt = 0
    for i in obj:
        if i == target:
            cnt += 1
    for i in range(cnt):
        obj.remove(target)
    return obj


def remover2(obj: list, target: int) -> list:
    cnt = obj.count(target)
    for i in range(cnt):
        obj.remove(target)
    return obj


def remover3(obj: list, target: int) -> list:
    while True:
        try:
            obj.remove(target)
        except:
            break
    return obj


if __name__ == "__main__":
    list_ = list(map(int, input().split()))
    tgt = int(input())
    print(remover3(list_, tgt))
