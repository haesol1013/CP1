"""""""""
# 이상치 검출 (Pandas)


## 설명
이상치는 데이터 집단에서 일반적인 분포외에 위치하는 값들을 의미합니다.
이런 값들은 데이터 분석에 편향을 일으키고, 인공지능 학습이 비정상적으로 이루어질 수 있는 요소로 작용합니다.
이상치를 제거할 수 있는 가장 간단한 방법은 표준편차를 이용하는 것입니다.
표준편차는 아래와 같이 정의됩니다.

image.png

어떤 값의 편차가 표준 편차보다 크다면 이상치로 판단할 수 있습니다.

image.png

이름을 outlier로 하고, 이상치인 지 아닌 지를 True/False 형태의 DataFrame으로 반환하는 함수를 정의하세요.

## 입력 설명
임의의 값들이 여러개의 속성에 생성된 DataFrame이 입력됩니다.

## 출력 설명
주어진 DataFrame에서 이상치인 것만 True로 하는 Boolean타입 DataFrame을 반환해야 합니다.


### 입력 예시 1 
    0    1    2
0   4    1    10
1   4.2  1.2  14
2   3.8  0    1000
3  -4    0.9  9 
### 출력 예시 1
    0    1    2
0   F    F    F
1   F    F    F
2   F    T    T
3   T    F    F 
"""""""""
import pandas as pd
import numpy as np


def outlier(df):
    return df - df.mean() >= df.std()
