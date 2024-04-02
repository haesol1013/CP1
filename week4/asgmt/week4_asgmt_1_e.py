def mod(num1, num2):
    opposite_sign = num1 * num2 < 0
    need_inverse = num2 < 0

    num1 = abs(num1)  # abs 함수 -> 넣은 숫자의 절댓값을 반환
    num2 = abs(num2)
    same_num = num1 == num2

    while num1 >= num2:
        num1 -= num2

    if opposite_sign and not same_num:
        num1 = num2 - num1

    if need_inverse:
        num1 *= -1

    return num1


a, b = map(int, input().split())
print(mod(a, b))

