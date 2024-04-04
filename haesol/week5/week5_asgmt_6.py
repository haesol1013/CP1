def standardization(input_list):
    micro = sum([i for i in input_list]) / len(input_list)
    sigma = sum([(i-micro)**2 for i in input_list]) / len(input_list)
    return [(i-micro) / (sigma**0.5) for i in input_list]


list_ = list(map(int, input().split()))
print(standardization(list_))
