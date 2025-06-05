"""""""""
# 정수강박증

## 설명
핀셋으로 쿼크를 수집하다가 집중력을 소진한 정성윤은 모든 숫자를 정수로만 봐야하는 강박증에 걸렸습니다.
성윤이를 위해 모든 숫자를 정수로만 걸러주는 함수를 작성하세요.
단, 데이터 타입이 변하지 않아야 합니다.

함수 이름은 only_integer로 합니다.
또, only_integer 내부에서 함수를 정의할 경우, lambda만 사용해야 합니다.

## 입력 설명
integer 또는 float 타입의 숫자들이 하나의 List로 입력됩니다.

## 출력 설명
integer든 float이든 오직 정수만 남긴 채 list로 반환해야 합니다.


### 입력 예시 1 
[1, 2.2, 4.0]
### 출력 예시 1
[1, 4.0]
"""""""""

def only_integer(arr: list[int | float]) -> list[int | float]:
    return [elem for elem in arr if int(elem) == elem]


if __name__ == "__main__":
    data = input()[1:-1].split(", ")
    arg1 = [float(elem) if "." in elem else int(elem) for elem in data]
    print(only_integer(arg1))
