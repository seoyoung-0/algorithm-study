# https://leetcode.com/problems/top-k-frequent-elements/
'''
- 빈도순 에서 k번 높은 요소까지 출력
'''

import collections
import heapq
class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Counter객체
        # heapq 사용 - min heap(키값 음수값으로 구성 -  가장 작은 것부터) ( 92ms )
        
        count = collections.Counter(nums)

        count_heap = []

        for c in count:
            heapq.heappush(count_heap, (-count[c], c))

        topk = list()
        for _ in range(k):
            topk.append(heapq.heappop(count_heap)[1]) ## heappop
        
        return topk
    
    """ # 파이썬 다운 풀이 - zip, * 활용
     return list(zip(*collections.Counter(nums).most_common(k)))[0]
    """
    
    
    """ 내 풀이 - value 로 sorted 하고 k 만큼 값 뽑기 ( 108ms )
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for index, n in enumerate(nums):
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        res = []
        
        count = sorted(count.items(),key = (lambda x:x[1]),reverse = True)
        
        for i in range(k):
            res.append(count[i][0])
        
        return res
    """


        
