"""""""""
# 연산 클래스


## 설명
연산을 위한 Class를 만들고자 합니다.
Class의 이름은 math로 하고 덧셈, 뺄셈, 곱셈, 나눗셈, 제곱, 제곱근 함수를 갖는 Class를 정의하세요.

## 조건
1. 덧셈 함수의 이름은 add, 뺄셈은 sub, 곱셈은 mul, 나눗셈은 div, 제곱은 pow, 제곱근은 root로 합니다.
2. Object가 생성될 때 연산에 사용할 두 값을 인자로 받고, 인자가 없을 경우 1을 기본 값으로 한다.
3. 덧셈, 뺄셈, 곱셈, 나눗셈, 제곱, 제곱근 함수는 인자를 받지 않는다.(self만 받을 것)
4. Object가 생성될 때 받은 두 인자 값을 속성으로 저장해두고 연산 함수가 호출될 때 해당 속성을 가져와 연산한다.
5. 제곱 및 제곱근 함수는 첫 번째 인자를 밑, 두 번째 인자를 지수로 사용한다.

## 입력 설명
두 자연수가 클래스 인자로 입력됩니다.

## 출력 설명
클래스의 덧셈, 뺄셈, 곱셈, 나눗셈, 제곱, 제곱근 출력이 정상적으로 이루어져야 합니다.


### 입력 예시 1 
m=math(10,2)
print(m.add())
print(m.div())
print(m.mul())
print(m.sub())
print(m.pow())
print(m.root())

### 출력 예시 1
12
5.0
20
8
100
3.1622776601683795


### 입력 예시 2 
m=math(2,5)
print(m.add())
print(m.div())
print(m.mul())
print(m.sub())
print(m.pow())
print(m.root())

### 출력 예시 2
7
0.4
10
-3
32
1.148698354997035
"""""""""


class math:
    def __init__(self, x=1, y=1):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mul(self):
        return self.x * self.y

    def div(self):
        return self.x / self.y

    def pow(self):
        return self.x ** self.y

    def root(self):
        return self.x ** (1/self.y)


if __name__ == "__main__":
    n1, n2 = map(int, input().split())
    cal = math(10, 2)
    print(cal.add())
    print(cal.div())
    print(cal.mul())
    print(cal.sub())
    print(cal.pow())
    print(cal.root())
