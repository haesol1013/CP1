"""""""""
Cyclic Maximum


설명
이름을 sinmax로 하고, 임의의 데이터프레임이 주어질 때 레코드 별 sin 최대값을 반환하는 함수를 정의하세요.

입력 설명
Pandas의 DataFrame 타입 변수 1개가 인자로 입력됩니다.

출력 설명
레코드 별 sin 최대값을 Iterable* 형태로 반환해야 합니다. (단, 소수점이 발생한 경우 ±0.001 까지 오차를 허용합니다.)

* List, Tuple, Pandas의 Series 모두 Iterable입니다.


입력 예시 1 
5 6 2
7 3 10
출력 예시 1
[0.909297, 0.656987]

힌트
※ df.apply 함수는 결과를 df에 inplace에 적용하지 않고 새로운 dataframe을 반환한다.
"""""""""
import pandas as pd
import numpy as np


def sinmax(df):
    return np.sin(df).max(axis=1)


if __name__ == "__main__":
    a = pd.DataFrame([[5, 6, 2], [7, 3, 10]])
    print(sinmax(a))
