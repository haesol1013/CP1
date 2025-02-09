"""""""""
# [기말-06]Vigenère Cipher


## 설명
비제네르 암호는 Caesar Cipher를발전시킨 다중 대치 암호 방식입니다. 시저 암호와는 달리, 비제네르 암호에서는 각 알파벳을 시프트하는 거리가 고정되지 않고 키(Key)에 따라 다르게 설정됩니다.
구체적인 방식은 아래와 같습니다.

C#으로 이해하는 암호학 미리보기 [교보 eBook]

이미지 출처 :http://preview.kyobobook.co.kr/epubPreviewPopup.jsp?type=web&barcode=4801191319188&search=Y

이름을 vigenere라고 하고, 평문과 Key가 들어왔을 때 이를 암호화하는 함수를 정의하세요.
(주의! Key 값 'a'는 0 부터 Shift 합니다.

## 입력 설명
첫 번째 인자로 평문이, 두 번째 인자로 Key가 주어집니다. (평문과 Key는 모두 소문자인 string 형태로 이루어져 있고, 평문의 길이와 Key의 길이는 항상 같습니다)

## 출력 설명
암호화된 문장을 string 형태로 반환하세요.


### 입력 예시 1 
'abcd','aaaa'
### 출력 예시 1
abcd

### 입력 예시 2 
'abcd','zzzz'
### 출력 예시 2
zabc

### 입력 예시 3 
'hello','abcde'
### 출력 예시 3
hfnos

## 힌트
ord(c)>문자를ASCII코드(int)로 변환하는 함수
chr(n)> ASCII코드(int)를문자로 변환하는 함수
"""""""""


def vigenere(word: str, key: str):
    ascii_list = []
    for chr1, chr2 in zip(word, key):
        ascii_ = ord(chr1) + ord(chr2) - 97
        ascii_ = ascii_ - 26 if ascii_ > 122 else ascii_
        ascii_list.append(ascii_)
    return "".join(map(chr, ascii_list))


if __name__ == "__main__":
    arg1 = input()
    arg2 = input()
    print(vigenere(arg1, arg2))
