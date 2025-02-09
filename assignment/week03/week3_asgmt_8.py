"""""""""
# 모음이 싫어!


## 설명
이제 막 알파벳을 배우기 시작한 다솜이는 알파벳 모음 조합에 따라 발음이 굉장히 달라지는 것에 스트레스를 받고 있습니다.
그래서 다솜이는 알파벳에 모음을 없애버리고자 하는 원대한 계획을 세웁니다.
다솜이를 도와 입력으로 주어지는String에 모음을 모두 없애 출력하세요. (단, 반모음인 w와 y는 모두 모음으로 간주하며 띄어쓰기는 유지해야 합니다.)

## 입력 설명
1개의 String이 주어집니다.
특수문자, 숫자 등을 제외한 오로지 알파벳으로만 주어집니다. 단, 대문자와 소문자가 구별되어 입력됩니다.

## 출력 설명
모음이 없는 String이 출력되어야 합니다.


### 입력 예시 1 
string
### 출력 예시 1
strng

### 입력 예시 2 
i dont care
### 출력 예시 2
 dnt cr
 
### 입력 예시 3 
Improve the Level
### 출력 예시 3
mprv th Lvl

## 힌트
정보) String도 Iterator다
Iterator에는 range, list, tuple, dictionary 등이 있다.
"""""""""

word = input()
vowel = "aeiouwyAEIOUWY"
print(''.join([i for i in word if i not in vowel]))
