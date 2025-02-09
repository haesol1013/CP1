"""""""""
# 주류 구분


## 설명
알콜도수로 주류를 구분하고, 주류 마다 맞는 특성을 가진 클래스를 만드시오.

## 요구 사항
1. 클래스가 생성될 때 알콜도수 alc를 입력 받습니다. 
(만약 alc가 40 이상이라면 Wiskey, 20이상 이라면 Port Wine, 10이상 이라면 Wine, 4이상 이라면 Beer로 분류합니다.)
2. 클래스를 print로 출력할 때 해당 주류가 무엇인지 출력합니다. ("Wiskey", "Port wine", "Wine", "Beer")
3. 클래스가 +연산을 만난다면, 주류 특성이 Trash로 바뀌어서 print할 때 "Trash"가 출력되어야 합니다.


### 3번 실행 예시
pritn(A) ==> "Wiskey"

### 4번 실행 예시
A+B
print(A) ==> "Trash"
"""""""""

from __future__ import annotations


class Beverage:
    def __init__(self, alc: float) -> None:
        if alc >= 40:
            self.type = "Wiskey"
        elif alc >= 20:
            self.type = "Port Wine"
        elif alc >= 10:
            self.type = "Wine"
        elif alc >= 4:
            self.type = "Beer"
        else:
            self.type = "None"

    def __str__(self) -> str:
        return self.type

    def __add__(self, other: Beverage) -> None:
        self.type = "Trash"
        other.type = "Trash"


bev_1 = Beverage(40)
bev_2 = Beverage(30)
print(bev_1)
print(bev_2)
bev_1 + bev_2
print(bev_1)
print(bev_2)