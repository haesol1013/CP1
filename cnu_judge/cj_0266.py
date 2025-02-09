"""""""""
# 회문 저장소


## 설명
문장 또는 숫자가 대칭을 이루는 구조를 회문(Palindrome)이라고 합니다.
예를 들어 LEVEL은 앞으로 읽으나 뒤로 읽으나 똑같으므로 회문입니다.

공항에서 물품보관소를 운영하는 독고고독 씨는 대칭을 이루는 물건이 아니면 보관하지 않습니다.
독고고독 씨를 위해 의뢰받은 물건(문장)이 대칭(회문)인 지 판단하고, 보관중인 물건(회문)의 수를 알려주는 클래스를 정의하세요.
Class의 이름은 palindrome으로 하고, 회문인지 판단하는 객체 함수의 이름을 check로 하는 Class를 정의하세요.

## 조건
1. Object로 생성될 때 발생하는 인자는 없다.
2. 회문 판단 객체 함수 check에 하나의 String이 인자로 주어지고, 회문이라면 클래스 속성 값에 카운트한다.
3. print( Object )를 실행했을 때, 현재 저장된 회문의 수를 출력하도록 한다.

## 입력 설명
클래스 인자는 입력되지 않고, 객체 함수 check에 임의의 문장이 입력됩니다.

(단, 문장은 띄어쓰기 없이 대문자 알파벳 만으로 입력됩니다.)

## 출력 설명
print 함수로 Object를 호출했을 때 회문의 개수가 출력되어야 합니다.


### 입력 예시 1 
p=palindrome()

p.check('LEVEL')
p.check('TOOTH')
p.check('RACECAR')

print(p)
### 출력 예시 1
2

## 힌트
객체 함수 __str__()은 print 등 출력될 때 실행해야할 내용을 정의한다.
"""""""""


class palindrome:
    def __init__(self):
        self.cnt = 0

    def check(self, word: str):
        if word == "".join(reversed(word)):
            self.cnt += 1

    def __str__(self):
        return str(self.cnt)


if __name__ == "__main__":
    p = palindrome()

    p.check('LEVEL')
    p.check('TOOTH')
    p.check('RACECAR')

    print(p)
