# 알리바바와 40인의 도둑_topdown

def dfs(i,j):
    
    if i == 0 and j == 0:
        return dy[i][j]
    
    if dy[i][j]: # 메모이제이션
        return dy[i][j]
    
    else:
        if j == 0:
            dy[i][j] = dfs(i-1,j) + block[i][j]
        elif i == 0:
            dy[i][j] = dfs(i,j-1) + block[i][j]
        else:
            dy[i][j] = block[i][j] + min(dfs(i,j-1),dfs(i-1,j))
        
        return dy[i][j]

n = int(input())
block = [list(map(int, input().split())) for _ in range(n)]
dy = [[0]*n for _ in range(n)]
dy[0][0] = block[0][0]

# 가장자리
# for i in range(n):
#     dy[0][i] = dy[0][i-1] +block[0][i]
#     dy[i][0] = dy[i-1][0] + block[i][0]
    
dfs(n-1,n-1)
