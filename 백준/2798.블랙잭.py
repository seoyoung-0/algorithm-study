#2798 블랙잭
import itertools

N,M = map(int, input().split())
card = list(map(int, input().split()))

nPr = list(itertools.permutations(card,3))
max_sum = 0

for i in range(len(nPr)):
    n_sum = sum(nPr[i])
    if n_sum > M:
        continue
    else:
        max_sum = max(max_sum, n_sum)
print(max_sum)
