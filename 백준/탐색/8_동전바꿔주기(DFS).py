# 동전 바꿔주기
# T=20, k=3가지 종류 동전
# 동전 값, 개수 입력 
# T 만들수있는 조합 가지수 

def dfs(remain, sub):
    if sum(sub) == T:
        if sub not in res:
            res.append(sub[:])
        return
    
    else:
        for i,n in enumerate(remain):
            sub.append(n)
            dfs(remain[i+1:],sub)
            sub.pop()


T = int(input())
k = int(input())
coin = []
res = []

for i in range(k):
    p,n = map(int,input().split())
    for j in range(n):
        coin.append(p)
coin.sort(reverse = True)
dfs(coin, [])
print(len(res))
