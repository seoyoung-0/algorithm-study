# 5. 가장 높은 탑 쌓기 
# 밑면 좁은 벽돌 위에 더 넓은 벽돌 쌓을 수 없음
# 무게가 무거운 벽돌을, 가벼운 벽돌 위에 놓을 수 없다.
# 가장 높은 높이

n = int(input())

# ( 밑면 넓이, 벽돌 높이, 무게 )
blocks = []
for i in range(n):
    s, h, w = map(int, input().split())
    blocks.append((s,h,w))

blocks.sort(key = lambda x:x[0],reverse = True) 
# 무게만 비교 + 높이 더하기 

dh = [0] * (n) 
# i번째 블록이 제일 위일때의 높이

height = 0
for i in range(0, n):
    max_height = 0
    
    for j in range(i-1,-1,-1):
        if blocks[i][2] < blocks[j][2]:
            max_height = max(max_height,dh[j])
            
    dh[i] = max_height + blocks[i][1]
    
print(max(dh))    
