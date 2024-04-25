"""""""""
# 정수만 입장하세요.


## 설명
데이터들이 모여 노는 클럽이 있다.
이 클럽에는 정수형 데이터만 들어갈 수 있다.
함수의 인자가 정수(int)가 아닌 경우 ValueError를 발생하고 "You can't enter here"라는 에러 메시지를 출력하는 함수를 완성하세요.
반드시 raise를 사용하세요.

## 입력 설명
1개의 인자가 함수에 입력됩니다.

## 출력 설명
입력된 인자가 int 타입이 아니라면 ValueError를 발생하고 에러 메시지로You can't enter here를 출력하세요.


### 입력 예시 1 
15
### 출력 예시 1
Welcome

### 입력 예시 2 
Can I?
### 출력 예시 2
ValueError : You can't enter here
"""""""""


def club_database(n):
    if type(n) != int:
        raise ValueError("You can't enter here")
    return "Welcome"


print(club_database(0))
