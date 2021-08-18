# 1697 숨바꼭질
# https://www.acmicpc.net/problem/1697
# - 일차원 BFS
from collections import deque

def next_num(x):
    res = []
    res.append(x-1)
    res.append(x+1)
    res.append(x*2)
    
    return res

def bfs(n):
    queue= deque()
    queue.append(n)
    
    while queue:
        x = queue.popleft()
        
        if x == K:
            print(numbers[x])
        else:
            next_num_list = next_num(x)
            for num in next_num_list:  
    #for num in (x-1, x+1, x*2) - 함수안쓰고 이렇게도 가능
                if 0<=num<=100000 and not numbers[num]:
                    numbers[num] = numbers[x] + 1
                    queue.append(num)        

N, K = map(int, input().split())
numbers = [0]* (100000+1)
bfs(N)
