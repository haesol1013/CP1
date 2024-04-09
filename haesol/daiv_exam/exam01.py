n, m, q = map(int, input().split())

side = list(range(1, n+1))
prob_side = list(map(int, input().split()))
summation = sum(prob_side)
probability = [element / summation for element in prob_side]


for case in range(q):
    question = int(input())


print(probability)
