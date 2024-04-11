

def instagram_debug(post_list: list, user_list: list) -> dict:
    set_ = set(zip(post_list, user_list))
    dict_ = {}

    for pairs in set_:
        post = pairs[0]

        if post not in dict_:
            dict_[post] = 1
        else:
            dict_[post] += 1

    return dict_


if __name__ == "__main__":
    posts = input().split()
    users = input().split()
    print(instagram_debug(posts, users))