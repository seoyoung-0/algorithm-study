# 유기농 배추

# 재귀 사용 시, 시간초과 안 나려면 recursionlimit

import sys
sys.setrecursionlimit(10000)

def dfs_bat(x,y):
    if x<0 or x>=m:
        return
    if y<0 or y>=n:
        return
    if bat[x][y] == 0:
        return

    bat[x][y] = 0

    dfs_bat(x,y+1)
    dfs_bat(x,y-1)
    dfs_bat(x+1,y)
    dfs_bat(x-1,y)
    
n = int(input())
for i in range(n):
    m,n,k = map(int, input().split())
    bat = [[0 for col in range(n)] for row in range(m)]
    count = 0 
    
    for j in range(k): # 배추 위치 표시
        x,y = map(int, input().split())
        bat[x][y] = 1
        
    
    for row in range(m):
        for col in range(n):
            if bat[row][col] == 1:
                dfs_bat(row,col)
                count += 1
                
    print(count)
