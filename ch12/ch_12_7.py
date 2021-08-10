# https://leetcode.com/problems/reconstruct-itinerary/
'''
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
'''
class Solution:
    
    from collections import defaultdict
      
# 재귀 - 리스트가 많을 때는 pop()이 O(1) 이므로 pop() 사용하는게 낫다
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:  
        
        graph = defaultdict(list)
        for f,t in tickets:
            graph[f].append(t)
        for f in graph:
            graph[f].sort(reverse=True) 
        print(graph)
        
        route = []
        def dfs(f):
            while graph[f]:
                dfs(graph[f].pop())
            print(route)
            route.append(f)
        
        dfs("JFK")
        return route[::-1]
        
        
# 재귀 
'''
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = defaultdict(list) ##list 인지 int 인지 
        for f,t in tickets:
            graph[f].append(t)
        for f in graph:
            graph[f].sort()
        
        route = []
        
        def dfs(f):
            while graph[f]:
                dfs(graph[f].pop(0))
            route.append(f)
        
        dfs("JFK")
        return route[::-1]    
'''    
    
# 반복 - 스택에 넣고 빼면서 route 에 추가
'''
    graph = defaultdict(list) ##list 인지 int 인지 
        for f,t in tickets:
            graph[f].append(t)
        for f in graph:
            graph[f].sort()
        
        route, stack = [], ['JFK']
        
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
                print(stack)
            route.append(stack.pop())
        return route[::-1]
        '''
