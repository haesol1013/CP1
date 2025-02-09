"""""""""
# [60점] 여기 제일 인싸가 누구야?


## 설명
하영채 선배는 친구가 많은걸 그리 좋아하지 않습니다.
그러다 문득 저택에서 홈파티를 열고 싶어져서 최대한 많은 친구들을 초대하고 싶어졌습니다.
그러나 다짜고짜 친하지 않은 친구가 초대하면 성공율이 매우 낮기 때문에 초대 성공율을 높이고자 전략을 구상했습니다.
하영채 선배의 전략은 친구를 가장 많이 가진 '인싸' 친구 단 한 명을 공략해 모두를 초대하는 것입니다.

그런데... 친구 사귀기를 좋아하지 않던 하영채 선배는 어떤 친구가 '인싸'인지 알 수 없었습니다.
하영채 선배를 위해 누가 가장 '인싸'인 지 알려주는 함수를 정의하세요.
함수의 이름은 insider로 합니다.
인싸 : 인사이더(Insider), 인간 관계가 매우 넓게 뻗어있는 사람

## 입력 설명
각 사람의 친구 목록은 set으로 구성되며, 이 목록들을 하나의 list로 구성해 함수에 입력됩니다.

## 출력 설명
가장 친구가 많은 사람의 이름을 반환합니다.
단, 친구 수가 같은 경우는 등장하지 않습니다.


### 입력 예시 1 
[ {'Mark', 'Bill'}, {'Mark', 'Kanye', 'Hiddleston'}, {'Mukyeom', 'Dasom', 'Mark'} ]
### 출력 예시 1
Mark
"""""""""


def insider(arr: list[set[str]]) -> str:
    all_mem = []
    for group in arr:
        for i in group:
            all_mem.append(i)
    set_mem = sorted(set(all_mem))
    cnt = [all_mem.count(i) for i in set_mem]
    return set_mem[cnt.index(max(cnt))]
