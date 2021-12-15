# 2503 숫자야구

from itertools import permutations
n = int(input())
data = [str(i) for i in range(1,10)]
nPr = list(permutations(data,3)) # 가능한 세자리수

for _ in range(n):
    num, strike, ball = map(int, input().split())
    number = list(str(num))
    removecount = 0
    for i in range(len(nPr)):
        s = b = 0
        i -= removecount # 앞에 없앤 개수만큼 i에서 빼주기 ***
        for j in range(3):
            if nPr[i][j] == number[j]:
                s += 1
                continue
            elif number[j] in nPr[i]:
                b += 1
                
        if (strike != s) or (ball != b):
            nPr.remove(nPr[i])
            removecount += 1 #
print(len(nPr))
