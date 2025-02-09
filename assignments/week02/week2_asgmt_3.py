"""""""""
# 2-Dimensional Gaussian Distribution


## 설명
1차원 정규분포 공식이 심심했던 영채는 2차원 정규분포를 알아보기로 했다.
영채는 구글링 끝에 다음과 같은 공식을 찾아냈고, 문득 이 분포를 파이썬으로 구현하고 싶어졌다.
영채를 도와 파이썬에 다음 공식을 구현해주자.
공식은 아래와 같다.
단,μ, ν, σ 는 random 모듈을 이용해 랜덤하게 생성되는 변수이며, 템플릿 코드에 이미 구현되어 있다. (-4≤μ≤ 4, -4≤ν≤ 4,1≤σ≤ 4)

2차원정규분포.png

## 입력 설명
첫째줄에 변수 x가 주어진다. (-32≤ x≤ 31)
두번째 줄에 변수 y가 주어진다. (-32≤ y≤ 31)

## 출력 설명
첫째 줄에 확률값 Z를 출력한다.


### 입력 예시 1 
8
-15
### 출력 예시 1
0.00015760456306063134

### 입력 예시 2 
30
-32
### 출력 예시 2
0.08423275429238294

## 힌트
Python의 math 모듈을 import해 다양한 함수를 사용해보자.
[참고]https://docs.python.org/ko/3/library/math.html- Python math module 공식 Docs
"""""""""

import math
import random

x = int(input())
y = int(input())

avg1 = random.randint(-4, 4)
avg2 = random.randint(-4, 4)
std1 = random.randrange(1, 5)
std2 = random.randrange(1, 5)

PI = math.pi

Z = (math.exp(-((x-avg1) / (2 * std1**2))) / math.sqrt(2 * PI * std1**2) *
     math.exp(-((y-avg2) / (2 * std2**2))) / math.sqrt(2 * PI * std2**2))

print(Z)
