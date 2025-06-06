"""""""""
# Polynomial Coefficient


## 설명
다항식은 여러가지의 차수로 이루어진 변수항들이 합해진 식입니다.
아래는 다항식 예시 중 하나입니다.

image.png

텍스트 표현법에서는 3*x^3+5.4*x^2+17*x^5-6으로 표현합니다.
이 때, 가장 높은 차수는 5이고 이의 계수는 17입니다.

함수의 이름은 polynomial이라고 하고, 다항식이 입력될 때 차수가 높은 순서대로 계수를 ','로 구분해 반환하는 함수를 정의하세요.
단, 상수는 계수로 보지 않으며, 차수가 1인 경우 '^' 기호 없이 'n*x'로만 표기합니다.
또, 계수가 0인 경우는 0으로 표기해야합니다.

## 입력 설명
수식이 표현된 String 하나가 인자로 입력됩니다.

## 출력 설명
차수가 높은 순서대로 계수를 ','로 구분되는 String으로 반환합니다.


### 입력 예시 1 
3*x^3+5.4*x^2+17*x^5-6
### 출력 예시 1
17,0,3,5.4,0

### 입력 예시 2 
2*x+3
### 출력 예시 2
2

### 입력 예시 3 
-x-1
### 출력 예시 3
-1

### 입력 예시 4 
6*x-7*x^6+2^2
### 출력 예시 4
7,0,0,0,0,6
"""""""""


def polynomial(expression: str) -> str:
    coefficients = {}
    start = 0
    for i, char in enumerate(expression):
        if char in "+-" and i > 0:
            _process_term(expression[start:i], coefficients)
            start = i
    _process_term(expression[start:], coefficients)

    if not coefficients:
        return ""

    max_degree = max(coefficients.keys())
    result = [coefficients.get(i, "0") for i in range(max_degree, 0, -1)]
    return ",".join(result)


def _process_term(term: str, coefficients: dict) -> None:
    if "x" not in term:
        return

    degree = int(term.split("^")[1]) if "^" in term else 1

    if "*" in term:
        coefficient = term.split("*")[0].lstrip("+")
    else:
        coefficient = "-1" if term.startswith("-") else "1"

    coefficients[degree] = coefficient


if __name__ == "__main__":
    test_cases = [
        "3*x^3+5.4*x^2+17*x^5-6",
        "2*x+3",
        "-x-1",
        "6*x-7*x^6+2^2",
        "2*x+1",
        "2*x^2",
        "+3"
    ]

    for case in test_cases:
        print(f"{case} >>> {polynomial(case)}")