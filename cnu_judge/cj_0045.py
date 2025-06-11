"""""""""
# SHA256

# 설명
SHA256은 대표적인 해시 암호 알고리즘입니다.
파이썬 라이브러리 hashlib을 사용해 SHA256 알고리즘을 손쉽게 사용할 수 있습니다.
이름을 hash로 하고, 평문과 암호문이 주어질 때 같은 의미를 가진 값인 지 비교하는 함수를 정의하세요.

## 입력 설명
첫 번째 인자로 Hash되지 않은 평문이 1개의 String으로 주어집니다.
두 번째 인자로 어떤 평문을 Hash한 것인 지 알 수 없는 암호문이 1개의 String으로 주어집니다.

## 출력 설명
평문과 암호문이 같은 의미를 가진 값이라면 'True'를 반환하고, 다른 의미를 가진 값이라면 'False'를 반환해야 합니다.


### 입력 예시 1 
apple
3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b
### 출력 예시 1
True

### 입력 예시 2 
apple
f223faa96f22916294922b171a2696d868fd1f9129302eb41a45b2a2ea2ebbfd
### 출력 예시 2
False

## 힌트
hashlib 라이브러리의 sha256함수는 일반적인 String을 받을 수 없으며, UTF-8로 번역된 문자열만 받을 수 있습니다.
String 객체의 encode() 함수는 String을 UTF-8로 인코딩해서 반환합니다.
"""""""""

import hashlib


def hash(word: str, hash_value: str) -> bool:
    return hashlib.sha256(word.encode()).hexdigest() == hash_value


if __name__ == "__main__":
    arg1 = input()
    arg2 = input()
    print(hash(arg1, arg2))
