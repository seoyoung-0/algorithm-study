# https://leetcode.com/problems/trapping-rain-water/
'''
투 포인터 사용
왼,오 max 에서 가운데로 오면서
작은 것들과의 높이 차이 파악하기
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0
        
        left, right = 0, len(height)-1
        left_max, right_max = height[left] , height[right]
        volume = 0 

        while left < right:
            left_max, right_max = max(left_max, height[left]),max(right_max, height[right])

            if left_max <= right_max:
                volume += (left_max - height[left])
                left += 1
            else:
                volume += (right_max - height[right])
                right -= 1
                
        return volume
