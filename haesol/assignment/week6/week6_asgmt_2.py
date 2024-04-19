"""""""""
# 교집합


## 설명
함수 이름을 intersection으로 하고, 인자로 주어지는 두 집합의 교집합을 반환하는 함수를 정의하세요.

## 입력 설명
2개의 set가 순서대로 함수 인자로 입력됩니다.
e.g. func(a=set, b=set)

## 출력 설명
입력된 두 인자의 교집합을 set로 반환합니다.


### 입력 예시 1 
{1, 2 ,3}
{3, 4, 5}
### 출력 예시 1
{3}

### 입력 예시 2 
{"T", 1, "CNU", "C"}
{"CNU", 2, "T"}
### 출력 예시 2
{"CNU", "T"}
"""""""""


def intersection(set_a: set, set_b: set) -> set:
    return set_a.intersection(set_b)


if __name__ == "__main__":
    set_a = set(input().split())
    set_b = set(input().split())
    print(intersection(set_a, set_b))
