# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
- sys 의 maxsize 로 바로 대체될 수 있는 min_price 선언
- min_price 갱신
- 최고점과 min_price 와의 차이, 즉 profit 갱신
'''

import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize # 44.5%
        # min_price = max(prices) # 37.5%

        for n in prices:
            min_price = min(n, min_price)
            profit = max(profit, n-min_price)
        
        return profit
    
    ''' <Time Limit Exceeded>
    
        max_res = 0
        for i in range(0,len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i] < prices[j]:
                    part = prices[j]- prices[i]
                    if max_res < part:
                        max_res = part
        return max_res
    '''
        
