"""""""""
# 그만빼가

## 설명
충남대학교 수석 보안관리자인 유채민은 암호화되지 않은 정보(Plain data)를 발견하였습니다.
5분 뒤 해커가 시스템을 점거한다는 소식을 사전 접수한 유채민을 도와 대량으로 데이터를 암호화시키는 함수를 map을 사용해 작성하세요.
함수 이름은 dont_steal_our_info로 합니다.

암호화를 위한 함수는 encrypt라는 이름으로 사전 정의 되어있습니다.

## 입력 설명
List 타입의 데이터 하나가 인자로 입력됩니다.
(list 값들은 int 타입입니다.)

## 출력 설명
암호화된 list를 반환합니다.
(list 값들은 string 타입입니다.)


### 입력 예시 1 
[1]
### 출력 예시 1
['ea591dc01371ff2']

### 입력 예시 2 
[1,2,3]
### 출력 예시 2
['ea591dc01371ff2', '460f39078f1cb6e3', '75b46ccfe7292a62']

### 입력 예시 3 
[34439512, 97638842]
### 출력 예시 3
['46d01372474b2e4', '6932c03ed4fd3cec']
"""""""""

def encrypt(x: int) -> str:
    return hex(abs(hash(str(x))))[2:]


def dont_steal_our_info(arr: list[int]) -> list[str]:
    return list(map(encrypt, arr))


if __name__ == "__main__":
    arg1 = list(map(int, input()[1:-1].split(",")))
    print(dont_steal_our_info(arg1))
