# 2178 - 미로탐색 
'''(0,0) -> (N,M) 으로 이동할 때 지나야 하는 최소의 칸 수 
인접한 칸으로만 이동 가능

BFS - 단순히 상하좌우로 방문X, 시작점으로부터 각 점들까지 거리계산
bfs 로 거리재기
'''
from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def miro_bfs(x,y):
    queue = deque()
    dist = 0 
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]

            if nx <0 or nx >= N or ny <0 or ny >= M:
                continue
            if board[nx][ny] == 0:
                continue
                
            if board[nx][ny] == 1:
                dist = board[x][y] + 1
                board[nx][ny] = dist
                queue.append((nx,ny))
                
N,M = map(int, input().split())
board = []
for i in range(N):
    numbers = str(input())
    row = []
    for s in numbers:
        row.append(int(s))
    board.append(row)
    
miro_bfs(0,0)
print(board[N-1][M-1])
