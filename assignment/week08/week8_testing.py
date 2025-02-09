def factorial(x):
    s = 1
    for i in range(x):
        # if i == 0:
        #     raise ValueError("There's 0!")
        assert i != 0, "There's 0!"
        s *= i
    return s


print(factorial(3))