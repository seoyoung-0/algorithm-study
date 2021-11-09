# 알리바바 -bottom_up
# dp 로 가장자리 걸리는 최소비용 
# -> n,n 까지 최소비용

n = int(input())

block = [list(map(int, input().split())) for _ in range(n)]
dy = [[0]*n for _ in range(n)]
dy[0][0] = block[0][0]

# 가장자리 
for i in range(n):
    dy[0][i] = dy[0][i-1] +block[0][i]
    dy[i][0] = dy[i-1][0] + block[i][0]

for i in range(1, n):
    for j in range(1,n):
        dy[i][j] = min(dy[i-1][j], dy[i][j-1])+block[i][j]

print(dy[n-1][n-1])

'''
def find_path(path,i,j):
    
    if i==n-1 and j==n-1:
        path += block[i][j]
        print(path)
        return path
    
    else:
        path += block[i][j]
        
        if i==n-1:
            ni,nj = i,j+1
        elif j ==  n-1:
            ni,nj = i+1, j
        else:
            next_right = block[i][j+1]
            next_down = block[i+1][j]

            if next_right < next_down:
                ni,nj = i,j+1
            else:
                ni,nj = i+1,j

        find_path(path, ni,nj)
'''
