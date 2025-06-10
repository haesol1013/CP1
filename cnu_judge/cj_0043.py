"""""""""
# Decode RLE

## 설명
Run-Length Encoding은 반복되는 문자를 병합해 개수로 나타내는 방법으로 데이터를 압축합니다.
예를 들어 'aaabbcde' 라는 문장을 'a3b2cde'로 압축할 수 있습니다.
이름을 decode로 하고, 함수 인자로 RLE 압축 문장이 주어질 때 원문으로 복원하는 함수를 정의하세요.

## 입력 설명
RLE로 압축된 문장이 1개의 String으로 함수 인자에 입력됩니다.

## 출력 설명
RLE 압축 문장을 원문으로 복원하여 반환해야 합니다.


### 입력 예시 1 
a3b2cde
### 출력 예시 1
aaabbcde

### 입력 예시 2 
w3navercom
### 출력 예시 2
wwwnavercom
"""""""""

def decode(string: str) -> str:
    result = []
    for char in string:
        try:
            num = int(char)
            for i in range(1, num):
                result.append(result[-1])
        except ValueError:
            result.append(char)
    return "".join(result)


if __name__ == "__main__":
    arg1 = input()
    print(decode(arg1))
