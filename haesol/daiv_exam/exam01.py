import sys


n, m, q = map(int, sys.stdin.readline().split())

side = list(range(1, n+1))
prob_side = list(map(int, sys.stdin.readline().split()))
summation = sum(prob_side)
probability = [element / summation for element in prob_side]


for case in range(q):
    question = int(sys.stdin.readline())


print(probability)