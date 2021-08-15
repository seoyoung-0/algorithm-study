# 7576 - 토마토 (완료)
'''
시작점 여러개 + 시작점부터 거리(==익는 데 걸리는 시간)
- 시작점들부터 큐에 넣고, 해당 큐에 bfs 진행하면
- 각 시작점에서 거리순으로 큐에 쌓이는 것
'''
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def tomato_bfs():
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx<0 or nx>=M or ny<0 or ny>=N:
                continue
            if board[nx][ny] == -1:
                continue
                
            if board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx,ny))
      
    
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(M)]
start = deque()

remain = False
res = -2
queue = deque()

# 시작점 start 라는 큐에 넣기
for i in range(M):
    for j in range(N):
        
        if board[i][j] == 1:
            queue.append((i,j))
            
tomato_bfs()

for i in board:
    print(i)
    for j in i:
        if j == 0:
            remain = True
        res = max(res, j)

if remain:
    print(-1)
elif res == -1:
    print(0)
else:
    print(res -1)
