from collections import defaultdict

n = int(input())
edge = int(input())

graph = defaultdict(list)

for i in range(edge):
    start, end = map(int, input().split(' '))
    graph[start].append(end)
    graph[end].append(start)
    
visited = [0] * n

def dfs(num,visited = []):
    visited.append(num)
    for w in graph[num]:
        if w not in visited:
            visited = dfs(w, visited)
    return visited

print(len(dfs(1)) -1 )
