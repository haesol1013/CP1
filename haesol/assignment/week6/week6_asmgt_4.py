

def instagram_debug(post_list: list, user_list: list) -> dict:
    pair_set = set(zip(post_list, user_list))
    cnt_dict = {}

    for pair in pair_set:
        post = pair[0]

        if post not in cnt_dict:
            cnt_dict[post] = 1
        else:
            cnt_dict[post] += 1

    return cnt_dict


def instagram_debug_1(post_list: list, user_list: list) -> dict:
    pair_set = set(zip(post_list, user_list))
    only_post = list(map(lambda x: x[0], pair_set))
    like_dict = dict()

    for post in set(post_list):
        like_dict[post] = only_post.count(post)

    return like_dict


def instagram_debug_2(post_list: list, user_list: list) -> dict:
    dict_ = dict()

    for post in set(post_list):
        dict_[post] = list(map(lambda x: x[0], set(zip(post_list, user_list)))).count(post)

    return dict_


def instagram_debug_3(a, b):
    return dict(zip(sorted(set(a)), [list(map(lambda x: x[0], set(zip(a, b)))).count(i) for i in sorted(set(a))]))


if __name__ == "__main__":
    posts = input().split()
    users = input().split()
    print(instagram_debug_3(posts, users))
