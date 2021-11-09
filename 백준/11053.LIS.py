# 11053

n = int(input())
num = list(map(int, input().split()))
dy = [0] * n # 각 수가 마지막일 때 길이

for i in range(0,len(num)):
    max_j = 0
    for j in range(i-1,-1,-1):
        if num[i]>num[j]:
            max_j = max(max_j,dy[j])
            
    dy[i] = max_j + 1

print(max(dy))
