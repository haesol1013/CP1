"""""""""
# 인스타그램 개발자 KMK


## 설명
충남대학교 출신인 김무겸은 인스타그램에서 개발자로 활동하며, 혁신적인 '좋아요' 집계 알고리즘을 설계했습니다.
그러나 너무나도 혁신적이었던 나머지 예상치 못한 오류가 발생하고 있습니다.
한 사람이 한 게시물에 대해 단 한 번만 '좋아요'를 누를 수 있지만, 여러 번 반복해서 누를 수 있게 된 것입니다.
머리가 새하얘진 김무겸 개발자는 1년째 이 문제를 해결하지 못하고 있습니다.
김무겸 개발자를 도와서 이 알고리즘을 완성하세요.

좋아요가 발생한 게시물 리스트post_list와 이에 매칭되는 좋아요를 누른 유저 ID 리스트user_list가 인자로 주어질 때, 
한 사람 당 한 번만 좋아요를 눌렀을 때의 진짜 좋아요 수를 Dictionary로 반환하세요.

단, 함수의 이름은 instagram_debug로 하세요.

반드시 Dictionary와 Set를 사용해야 합니다.
Dictionary 또는 Set을 생성할 때, '{}' 대신 'dict()'와 'set()'을 사용하길 권장합니다.


## 입력 설명
게시물 리스트post_list와 1대1 매칭되는 좋아요를 누른 유저 ID 리스트user_list가 인자로 주어집니다.
예를 들어, 'A'라는 게시물에 '1', '2' 유저가 좋아요를 각각 1번 클릭했다면 다음과 같습니다.
post_list= ['A', 'A']
user_list= ['1', '2']

또, 'A', 'B'라는 게시물에 '1' 유저가 좋아요를 각각 2번, 3번 클릭했다면 다음과 같습니다.
post_list= ['A', 'A', 'B', 'B', 'B']
user_list= ['1', '1', '1', '1', '1']


## 출력 설명
각 게시물에 대해 진짜 좋아요 수를 Dictionary로 반환해야 합니다.

입력이 다음과 같다면
post_list= ['A', 'A', 'B', 'B', 'B', 'C', 'C']
user_list= ['1', '1', '1', '1', '1', '1', '2']

출력은 다음과 같아야 합니다.
return{'A':1, 'B':1, 'C':2}


### 입력 예시 1 
['A', 'A', 'B', 'B', 'B', 'C', 'C']
['1', '1', '1', '1', '1', '1', '2']
### 출력 예시 1
{'A':1, 'B':1, 'C':2}

### 입력 예시 2 
['A', 'A', 'B', 'B', 'B']
['1', '1', '1', '1', '1']
### 출력 예시 2
{'A':1, 'B':1}

### 입력 예시 3 
['A', 'A']
['1', '2']
### 출력 예시 3
{'A':2}
"""""""""


def instagram_debug(post_list: list, user_list: list) -> dict:
    pair_set = set(zip(post_list, user_list))
    like_dict = dict()

    for post in set(post_list):
        like_dict[post] = len([0 for pair in pair_set if pair[0] == post])

    return like_dict


def instagram_debug_1(post_list: list, user_list: list) -> dict:
    pair_set = set(zip(post_list, user_list))
    cnt_dict = dict()

    for pair in pair_set:
        post = pair[0]

        if post not in cnt_dict:
            cnt_dict[post] = 1
        else:
            cnt_dict[post] += 1

    return cnt_dict


def instagram_debug_2(a, b):
    return dict(zip(sorted(set(a)), [list(map(lambda x: x[0], set(zip(a, b)))).count(i) for i in sorted(set(a))]))


if __name__ == "__main__":
    posts = input().split()
    users = input().split()
    print(instagram_debug(posts, users))
