'''
[프로그래머스]
스택/큐 - 주식가격
- 가격이 떨어질 때 까지 몇 초 걸렸는지
'''

def solution(prices):

    answer = [0]*len(prices)
    stack = []

    for i,p in enumerate(prices):

        while stack and prices[stack[-1]] > p:
            top = stack.pop()
            answer[top] = i - top

        stack.append(i)

    while stack: # 끝날때까지 
        top = stack.pop()
        res = (len(prices)-1) - top
        answer[top] =res
    
    return answer
