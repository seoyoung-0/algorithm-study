# 인접행렬_경로탐색
from collections import defaultdict

def dfs(sub, v):
    if v == 5:
        print(sub)
        return
    
    for w in graph[v]:
        if w not in visited:
            sub.append(w)
            visited.append(w)
            dfs(sub,w)
            sub.pop()
            visited.pop()
                
N,M = map(int, input().split())
graph = defaultdict(list)

for i in range(M):
    s,d = map(int, input().split())
    graph[s].append(d)
    
# 1번에서 5번으로 가는 가지수 출력
visited = [1]
dfs([1], 1)
