"""""""""
# 겹치는 값 제거


## 설명
함수 이름을 unique로 하고, 2개의 List 인자에서 겹치는 값들을 삭제하고 하나로 합한 집합을 반환하는 함수를 정의하세요.

## 입력 설명
2개의 List가 함수 인자로 입력됩니다.

## 출력 설명
2개의 인자에서 겹치는 값을 삭제하고 하나로 합한 집합을 반환합니다.


### 입력 예시 1 
[1, 2, 3]
[3, 4, 5, 6]
### 출력 예시 1
{1, 2, 4, 5, 6}

### 입력 예시 2 
['T', 'CNU', 135, 6723]
[672, 135, 'T', 't']
### 출력 예시 2
{672, 6723, 'CNU', 't'}

## 힌트
1. set( LIST ) 함수를 이용하면 Set 타입으로 캐스팅할 수 있다.
"""""""""


def unique(list_a: list, list_b: list) -> set:
    return set(list_a).symmetric_difference(list_b)


if __name__ == "__main__":
    list_a = input().split()
    list_b = input().split()
    print(unique(list_a, list_b))



