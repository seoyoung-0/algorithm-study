# https://leetcode.com/problems/daily-temperatures/
'''
스택에 온도 인덱스 저장
스택의 온도보다 높은 온도 등장하면, 스택 내 작은 온도들과의 차 구해서
작은 온도 인덱스에 차 저장
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(temperatures)

        for i,t in enumerate(temperatures):

            while stack and t > temperatures[stack[-1]]:

                top = stack.pop()
                res[top] = i - top

            stack.append(i)
            
        return res
        
