"""""""""
# [기말-05]The Efficiency of Run-Length Encoding


## 설명
Run-Length Encoding(RLE)은 반복되는 문자를 병합해 개수로 나타내는 방법으로 데이터를 압축합니다.
예를 들어 'aaabbcde' 라는 문장을 'a3b2cde'로 압축할 수 있습니다.
여기서 'aaabbcde'의 길이는 8, 압축된 후 'a3b2cde'는 길이가 7이므로 압축율은 0.125( or 12.5%)입니다.
이름을 efficiency로 하고, 평문이 주어질 때 RLE로 압축 후 압축율에 따라 1, 2, 3 등급으로 구분하여 해당 등급을 반환하려고 합니다.
압축율(c)에 따른 등급에 관한 정의는 다음과 같습니다.

0 <= c <= 0.2 : 3
0.2 < c <= 0.4 : 2
0.4 < c < 1 : 1

허용 라이브러리 : math, numpy

## 입력 설명
하나의 String타입 문장이 인자로 주어집니다.

## 출력 설명
해당하는 등급을 int 형태로 반환합니다.


### 입력 예시 1 
aaaabbbb
### 출력 예시 1
1

### 입력 예시 2 
abcd
### 출력 예시 2
3
"""""""""


def efficiency(word: str):
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
    c = 1 - (len(result) / (len(word) - 1))

    if 0 <= c <= 0.2:
        return 3
    elif 0.2 < c <= 0.4:
        return 2
    else:
        return 1


if __name__ == "__main__":
    arg = input()
    print(efficiency(arg))
