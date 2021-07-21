# https://leetcode.com/problems/product-of-array-except-self/
'''
nums 의 수 제외하고 만들어질 수 있는 곱의 결과 찾기
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        # 자기 기준 왼쪽 곱들만 모아놓기
        p = 1
        for i in range(0,len(nums)):
            output.append(p)
            p = p * nums[i]

        p = 1
        # 왼쪽 곱들 모아놓은 것에 거꾸로 
        # 자기 기준 오른쪽 곱 곱해주기 - output 값 수정
        for j in range(len(nums)-1,-1,-1):
            output[j] = output[j] * p
            p = p * nums[j]
        return output

    
''' <O(n) 초과>
        output=[]
        for i,n in enumerate(nums):
            left, right = 0,len(nums)-1
            res = 1

            while left < i:
                res *= nums[left]
                left+= 1
            while right > i:
                res *= nums[right]
                right -=1
            output.append(res)
        return output
'''
