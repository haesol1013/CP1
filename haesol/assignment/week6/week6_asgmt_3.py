"""""""""
# Phonetic Alphabet


## 설명
군대나 경찰 등 정확한 음성 전달이 중요한 집단에서는 Phonetic Alphabet을 이용합니다.
Phonetic Alphabet이란 N과 M 같이 발음이 비슷한 단어끼리의 혼동을 막기 위해 N은 November, M은 Mike 등 알파벳-단어로 매칭된 코드입니다.
예를 들어 적을 제압했다는 의미로 'Target Down'을 전달하려면, Target을 한 글자로 줄여 T로하고, T를 Phonetic Alphabet으로 변환하면 Tango가 되므로 'Tango Down'으로 전달합니다.
함수 이름을 phonetic으로 하고, 입력으로 주어지는 알파벳들을 Phonetic Alphabet으로 변환해 띄어쓰기로 구분해 리스트로 반환하는 함수를 정의하세요.
단, 딕셔너리가 사용되어야 합니다.

## 입력 설명
함수 인자로 1개의 String이 주어집니다.
띄어쓰기는 없으며 모두 대문자 알파벳으로 구성되어 있습니다.

## 출력 설명
입력된 알파벳 String을 Phonetic Alphabet으로 변환하고 띄어쓰기로 구분하여 반환합니다.


### 입력 예시 1 
AI
### 출력 예시 1
Alpha India

### 입력 예시 2 
GETIT
### 출력 예시 2
Golf Echo Tango India Tango

## 힌트
1. String은 Iterable 이므로 for문을 사용할 수 있다.
2. ' '.join( LIST )로 하면 띄어쓰기를 사이사이에 끼워넣어 String으로 변환할 수 있다.
"""""""""


def phonetic(value: str) -> str:
    alphabet = {"A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo",
                "F": "Foxstrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliet",
                "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar",
                "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango",
                "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-Ray", "Y": "Yankee", "Z": "Zulu"}
    return ' '.join([alphabet[key] for key in value])


if __name__ == "__main__":
    a = input()
    print(phonetic(a))

