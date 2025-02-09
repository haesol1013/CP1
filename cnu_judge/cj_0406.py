"""""""""
# [기말-06]Standardization

## 설명
데이터의 분포를 일정한 형태를 유지하는 것은 패턴 파악 및 학습에 중요한 역할을 합니다.
예를 들어, 사람 키 데이터의 경우 150~190 사이에 분포하는데 160~170을 기준으로 밀집되어 있기 때문에 편향되어 있다고 볼 수 있습니다.
만약 데이터를 0을 기준으로 분포되도록 조정하면, 이 데이터의 패턴을 쉽게 파악할 수 있습니다.
분포를 조정하는 방법은 여러가지가 있지만 일반적으로 가장 많이 사용되는 방법은 표준편차를 이용하는 표준화(Standardization)이 있습니다.
Standardization은 아래와 같은 식을 따라 적용됩니다.

image.png

함수의 이름을 standardization으로 하고, 입력된 인자를 표준화시켜 반환하는 함수를 정의하세요.

허용 라이브러리 : Numpy, math

## 입력 설명
Float타입 Numpy array가 1차원(Vector)형태로 주어집니다.

## 출력 설명
표준화를 거친 결과를 Numpy array 또는 Iterable 형태로 반환해야 합니다.


### 입력 예시 1 
1,2,3,4,5
### 출력 예시 1
-1.41421356, -0.70710678,  0.        ,  0.70710678,  1.41421356

### 입력 예시 2 
100, 0
### 출력 예시 2
1, -1
"""""""""
import numpy as np


def standardization(arr):
    mu = arr.mean()
    std = np.sum((arr - mu)**2) / arr.size
    return (arr - mu) / std**0.5


if __name__ == "__main__":
    arg = [1,2,3,4,5]
    arg = np.array(arg)
    print(standardization(arg))
