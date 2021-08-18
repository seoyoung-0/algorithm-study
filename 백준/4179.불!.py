
# 4179 불! 
# https://www.acmicpc.net/problem/4179
'''
불에 대한 BFS 와 지훈이에 대한 BFS 를 모두 돌리기
- 불에 대한 BFS : 각 칸에 불이 전파되는 시간 먼저 다 구해두기
- 지훈이 BFS..불 나거나 이전에 불이 붙는다면 못가게 
'''
from collections import deque


dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs():
    # 불 먼저 BFS-F로 바뀌고, 지훈이 위치 CHECK 에 증가
    
    fqlen = len(fq)
    while fqlen:
        x,y = fq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if board[nx][ny] == '.':
                    board[nx][ny] = 'F'
                    fq.append([nx,ny])
        fqlen -= 1

    qlen = len(q)
    while qlen:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                print(check[x][y])
                return
            else:
                if board[nx][ny] == '.' and not check[nx][ny]:
                    check[nx][ny] = check[x][y] + 1
                    q.append([nx,ny])
                    
        qlen -= 1
        
    if q:
        bfs()
    else:
        print('IMPOSSIBLE')


R,C = map(int, input().split())
check = [[0]*C for _ in range(R)]

board,q,fq = [],deque(),deque()

for i in range(R):
    row = list(input().strip())
    board.append(row)
    for j, key in enumerate(row):
        if key =='J':
            q.append([i,j])
            check[i][j] = 1
            board[i][j] = '.'
        if key == 'F':
            check[i][j] = 1
            fq.append([i,j])

bfs()
