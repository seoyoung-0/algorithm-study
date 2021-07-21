# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n^2)...

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]




# 조회 개선 / 인덱스 : enumerate 사용하기
                
def twoSum(self, nums: List[int], target: int) -> List[int]:
    
    nums_map={}

    for i,num in enumerate(nums):
        if target - num in nums_map:
            return ([nums_map[target-num],i])
        nums_map[num] = i
