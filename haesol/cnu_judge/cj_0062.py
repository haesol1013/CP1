"""""""""
# [30점] Decode double-shifter Caesar Cipher


## 설명
Caesar Cipher는 알파벳을 3자리씩 밀어 쓰는 방법(Shift)으로 암호문을 작성합니다.
조금 더 보안성을 높이기 위해 2개의 Shift를 사용할 수 있습니다.
예를 들어 첫 번째 Shift가 3, 두 번째 Shift가 5라면
첫 번째 알파벳에서 3자리를 밀고, 두 번째 알파벳에서 5자리를 밀고, 세 번째 알파벳에서 3자리를 미는 식으로 Shift 2개를 반복해 암호화합니다.

image.png

이름을 caesar라고 하고,알파벳을 N, M자리씩 밀어 쓴 암호문을 해독하는 함수를 정의하세요.

허용 라이브러리 : math, numpy

## 입력 설명
첫 번째 인자로 Shifter 2개가 들어있는 리스트 [N,M],두 번째 인자로 암호문이 함수에 입력됩니다.
(Shifter 값 N,M은 모두 0 이상 정수로 주어지며, 모든 문자열은 소문자로 주어집니다.)

## 출력 설명
첫 번째 인자로 주어진리스트에 들어있는 순서대로 Shift해서Caesar Cipher를 해독한 평문을 반환해야 합니다.


### 입력 예시 1 
[3, 5]
ffhxdw
### 출력 예시 1
caesar

### 입력 예시 2 
[13, 25]
qnbmtrvk
### 출력 예시 2
doongsil
"""""""""
import math
import numpy as np


def caesar(lst: list, word: str):
    n, m = lst
    ord_list = list(map(ord, word))
    for idx, val in enumerate(ord_list):
        ord_list[idx] = val - n if idx % 2 == 0 else val - m
    for idx, val in enumerate(ord_list):
        if val < 97:
            ord_list[idx] = val + 26
    return "".join(map(chr, ord_list))


if __name__ == "__main__":
    arg1 = [13, 25]
    arg2 = "qnbmtrvk"
    print(caesar(arg1, arg2))
