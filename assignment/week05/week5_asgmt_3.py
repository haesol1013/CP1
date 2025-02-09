"""""""""
# Tuple 결합


## 설명
Tuple은 원소의 순서, 크기, 값 모두 변할 수 없는 객체입니다.
함수의 이름을 concat으로 하고, 2개의 인자를 입력받아 2개의 Tuple을 하나로 합쳐 반환하는 함수를 정의하세요.

## 입력 설명
2개의 Tuple이 concat 함수의 인자로 입력됩니다.

## 출력 설명
2개의 Tuple을 합쳐 하나의 Tuple을 반환해야 합니다. (Tuple이어야 합니다.)
순서대로 A, B가 입력된다면 A, B가 순서대로 결합되어야 합니다.


### 입력 예시 1 
1 2
3 4
### 출력 예시 1
(1, 2, 3, 4)

### 입력 예시 2 
1 2 3 4 5 6
7
### 출력 예시 2
(1, 2, 3, 4, 5, 6, 7)

힌트
### Tuple은 변할 수 없지만 List는 변할 수 있습니다.
"""""""""


if __name__ == "__main__":
    tuple_a = tuple(map(int, input().split()))
    tuple_b = tuple(map(int, input().split()))
    print(concat(tuple_a, tuple_b))
