from collections import deque

dx = [0,0,1,-1]
dy = [-1,1,0,0]

n = int(input())
board=[]
for i in range(n):
    board.append(list(map(int, input())))

def bfs(x,y):
    cnt = 1
    queue = deque()
    queue.append((x,y))
    board[x][y] = 0 
    
    while queue:
        
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<n and board[nx][ny] == 1:
                cnt += 1
                board[nx][ny] = 0
                queue.append((nx,ny))
                
    return cnt


num_list = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            num_list.append(bfs(i,j))
            
num_list.sort()
print(len(num_list))
for num in num_list:
    print(num)
