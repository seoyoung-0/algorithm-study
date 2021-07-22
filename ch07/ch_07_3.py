# https://leetcode.com/problems/3sum/

'''
i 는 그냥 증가, j,k 대신 투 포인터 사용한다.
-> O(N^3) 을 O(N^2) 로 풀이
- 투 포인터는 주로 "정렬"된 배열을 대상으로 한다.
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum > 0:
                    right -= 1
                elif sum < 0 :
                    left += 1
                else:
                    res.append([nums[i],nums[left],nums[right]])

                    while left < right and nums[left]==nums[left+1]:
                        left += 1
                    while left < right and nums[right]==nums[right-1]:
                        right -= 1

                    left +=1
                    right -=1
                        
        return res
    
    
    
''' 3 포인터 -> 타임아웃

nums.sort()
res = []

for i in range(len(nums)-2):
    if i > 0 and nums[i]==nums[i-1]:
        continue
    for j in range(i+1, len(nums)-1):
        if j > i+1 and nums[j] == nums[j-1]:
            continue
        for k in range(j+1, len(nums)):
            if k > j+1 and nums[k] == nums[k-1]:
                continue
            if nums[i] + nums[j]+nums[k] == 0 :
                res.append([nums[i],nums[j],nums[k]]

return res
 '''   
