# 1. 최대점수 구하기
# 제한시간 m 안에 n 개의 문제중 최대점수 얻을수 있게

def dfs(remain,sub,total_time,sub_sum):
    
    if total_time == M:
        global max_score
        max_score = max(max_score, sum(sub))
        return
    
    else:
        for i,n in enumerate(remain):
            sub.append(n[0])
            sub_sum += n[0]
            total_time += n[1]
            
            dfs(remain[i+1:],sub, total_time,sub_sum)
            sub.pop()
            total_time -= n[1]
            sub_sum -= n[0]
            
N,M = map(int, input().split())
s = []
for i in range(N):
    score, time = map(int, input().split())
    s.append((score, time))

s = sorted(s, key = lambda x:x[0],reverse =True)
max_score,total_time = 0,0
sub_sum = 0 
dfs(s,[],0,0)
print(max_score)
