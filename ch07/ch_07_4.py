# https://leetcode.com/problems/array-partition-i/

'''
두 수의 min 들로 구성된 합의 max - 정렬 활용하기
'''

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        return sum(sorted(nums)[::2])
  

'''
        part = []
        sum = 0
        nums.sort()

        for n in nums:
            part.append(n)

            if len(part) == 2:
                sum += min(part)
                part = []

        return sum  
'''
        
