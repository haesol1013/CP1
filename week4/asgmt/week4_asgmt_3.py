def gcd(num1, num2):
    s_num = num1 if num1 <= num2 else num2
    cd = []
    for i in range(1, s_num+1):
        if num1 % i == 0 and num2 % i == 0:
            cd.append(i)

    return cd[-1]

# [::1], 유클리드 호제법