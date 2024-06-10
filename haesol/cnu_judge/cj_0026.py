"""""""""
# Alias 검증


## 설명
함수의 이름을 check로 하고, 2개의 인자를 입력받아 Alias인 지 반환하는 함수를 정의하세요.

## 입력 설명
정해지지 않은 타입의 무작위 값을 가진 인자 2개가 check 함수에 입력됩니다.

## 출력 설명
두 인자가 Aliasing인지 확인하여 Aliasing이라면 'True'를 반환하고, 아니라면 'False'를 반환해야 합니다.

Aliasing : 변수 명은 다르지만 가르키는 값은 같은 상황


### 입력 예시 1 
a b
### 출력 예시 1
True

### 입력 예시 2 
a c
### 출력 예시 2
False

## 힌트
id() 함수는 변수의 진짜 이름(주소)을 보여줍니다.
"""""""""


def check(param1, param2):
    return id(param1) == id(param2)
