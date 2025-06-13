"""""""""
# Decode Caesar Cipher

## 설명
Caesar Cipher는 알파벳을 3자리씩 밀어 쓰는 방법으로 암호문을 작성합니다.
이름을 caesar라고 하고,알파벳을 N자리씩 밀어 쓴 암호문을 해독하는 함수를 정의하세요.

## 입력 설명
첫 번째 인자로 전위된 알파벳 자릿수 N, 두 번째 인자로 암호문이 함수에 입력됩니다.

## 출력 설명
Caesar Cipher를 해독한 평문을 반환해야 합니다.


### 입력 예시 1 
3
fdhvdu
### 출력 예시 1
caesar

### 입력 예시 2 
13
qbbatfvy
### 출력 예시 2
doongsil

힌트
ord(c)>문자를ASCII코드(int)로 변환하는 함수
chr(n)> ASCII코드(int)를문자로 변환하는 함수
"""""""""

def caesar(n: int, decoded_word: str) -> str:
    ord_list = list(map(ord, decoded_word))
    for i, code in enumerate(ord_list):
        ord_list[i] = ord("z")-(n-(code-ord("a")))+1 if code-n < 97 else code - n
    return "".join(map(chr, ord_list))


if __name__ == "__main__":
    arg1 = int(input())
    arg2 = input()
    print(caesar(arg1, arg2))
