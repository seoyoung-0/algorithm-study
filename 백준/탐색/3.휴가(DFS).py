# 2. 휴가(DFS)
''' 입력 : 7일, 상담별 걸리는 날짜와 상담금액
7
4 20
2 10
3 15
3 20
2 30
2 20
1 10
'''
def dfs(remain, sub, sub_total):
    
    global max_total
    global flag
    
    max_total = max(max_total, sub_total)
    
    for i, n in enumerate(remain):
        flag = True
        if n[0] + n[1] > N: # N일 초과할 경우
            continue
            
        for r in range(n[0],n[0]+n[1]):
            if reserved[r] != 0:
                flag = False
                    
        if flag is False:
            continue
            
        else:
            sub.append(n)
            sub_total += n[2]
            for j in range(n[0],n[0]+n[1]):
                reserved[j] = 1  # 예약
            dfs(remain[i+1:], sub, sub_total)
            
            
N = int(input())
info = []
for i in range(N):
    t,p = map(int, input().split())
    info.append((i,t,p))
    
flag = True
reserved = [0] * N
info = sorted(info,key = lambda x:x[2],reverse=True)
max_total,sub_total = 0,0
dfs(info,[],0)
print(max_total)
