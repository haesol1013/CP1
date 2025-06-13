"""""""""
# [30점] The Efficiency of Run-Length Encoding

## 설명
Run-Length Encoding(RLE)은 반복되는 문자를 병합해 개수로 나타내는 방법으로 데이터를 압축합니다.
예를 들어 'aaabbcde' 라는 문장을 'a3b2cde'로 압축할 수 있습니다.
여기서 'aaabbcde'의 길이는 8, 압축된 후 'a3b2cde'는 길이가 7이므로 압축율은 0.125( or 12.5%)입니다.

이름을 efficiency로 하고, 평문이 주어질 때 RLE로 압축 후 압축율을 반환하는 함수를 정의하세요.

허용 라이브러리 : math, numpy

## 입력 설명
하나의 String타입 문장이 인자로 주어집니다.

## 출력 설명
RLE로 압축했을 때의 압축율을 0~1 범위로 나타내 반환해야 합니다.
(단, 0.000001 미만의 오차는 허용됩니다.)


### 입력 예시 1 
aaaabbbb
출력 예시 1
0.5

### 입력 예시 2 
abcd
### 출력 예시 2
0

### 입력 예시 3 
aaabb
### 출력 예시 3
0.2
"""""""""

def efficiency(word: str) -> float:
    word += "?"
    target = word[0]
    streak = 1
    result = ""
    for chr_ in word[1:]:
        if chr_ == target:
            streak += 1
        else:
            result += target + str(streak) if streak > 1 else target
            target = chr_
            streak = 1
    return 1 - len(result) / (len(word)-1)


if __name__ == "__main__":
    arg = input()
    print(efficiency(arg))
