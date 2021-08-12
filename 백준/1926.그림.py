# 1926 그림 
'''
- 그림의 개수 랑 그림 중 넓이가 가장 넓은 것의 넓이 출력
- 1 로 연결된 것을 한 그림이라고 정의 

* 아무것도 없을 때 고려하기
'''

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs_pic(x,y):
    q = deque()
    q.append((x,y))
    board[x][y] = 2
    
    square = 1
    
    while q:
        x_,y_ = q.popleft()
        
        for i in range(4):
            nx = x_ + dx[i]
            ny = y_ + dy[i]
            
            if nx <0 or nx >= n or ny <0 or ny >= m:
                continue
            if board[nx][ny] == 0:
                continue
            if board[nx][ny] == 1: 
                # 갈 수 있는 곳
                q.append((nx,ny))
                square += 1
                board[nx][ny] = 2
    else:
        size_list.append(square)
        return 
#     return square

n, m = map(int, input().split())
board  = [list(map(int, input().split())) for _ in range(n)]

# for i in range(n):
#     row = list(map(int, input().split()))
#     board.append(row)
    
cnt,fin = 0,0

size_list = []
for i in range(n):
    for j in range(m):
        if board[i][j] ==1 : # 여러개의 시작점들
            bfs_pic(i,j)
            cnt += 1

print(cnt)
print(max(size_list) if size_list else 0)
