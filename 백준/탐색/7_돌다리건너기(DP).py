# 계단오르기
# n 계단을 1개씩 또는 2개씩 올라가는 방법 

def dfs(x):
    
    if s[x]:
        return s[x]
    
    if x == 1 or x == 2:
        return x
    else:
        s[x] = dfs(x-1) + dfs(x-2)
        return s[x]

n = int(input())
s = [0] * (n+1) # dynamic 배열 
print(dfs(n))
