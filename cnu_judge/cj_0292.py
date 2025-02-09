"""""""""
# 이상치 검출


## 설명
이상치는 데이터 집단에서 일반적인 분포외에 위치하는 값들을 의미합니다.
Examples of various outliers found in regression analysis. Case 1 is an...  | Download Scientific Diagram
이런 값들은 데이터 분석에 편향을 일으키고, 인공지능 학습이 비정상적으로 이루어질 수 있는 요소로 작용합니다.
이상치를 제거할 수 있는 가장 간단한 방법은 표준편차를 이용하는 것입니다.
표준편차는 아래와 같이 정의됩니다.

image.png

어떤 값의 편차가 표준 편차보다 크다면 이상치로 판단할 수 있습니다.

image.png

이름을 outlier로 하고, 이상치인 지 아닌 지를 True/False 배열로 반환하는 함수를 정의하세요.

## 입력 설명
랜덤한 값들이 들어있는 Numpy array가 하나의 인자로 주어집니다.

## 출력 설명
주어진 Array에서 이상치인 것만 True로 하고, 입력과 동일한 형태의 배열을 반환해야 합니다.


### 입력 예시 1 
[0.5, 0.3, 0.1, 0.2, 10.0]
### 출력 예시 1
[False, False, False, False, True]
"""""""""
import numpy as np


def outlier(arr):
    return arr - np.mean(arr) >= arr.std()


if __name__ == "__main__":
    arg = [0.5, 0.3, 0.1, 0.2, 10.0]
    arg = np.array(arg)
    print(outlier(arg))
