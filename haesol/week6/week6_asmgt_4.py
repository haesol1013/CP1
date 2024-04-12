

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


if __name__ == "__main__":
    posts = input().split()
    users = input().split()
    print(instagram_debug(posts, users))
