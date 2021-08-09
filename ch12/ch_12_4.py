# https://leetcode.com/problems/combinations/
'''
Input: n = 4, k = 2
Output:
[
  [2,4],[3,4],[2,3],[1,2],[1,3],[1,4],
]
'''
class Solution:
    
# solution 1 - itertools : 76ms

    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i+1 for i in range(n)]
        return list(combinations(nums, k))
    
# solution 2 - 인덱스 말고 숫자로 바로 접근 : 452ms

    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i+1 for i in range(n)]
        result = []

        def dfs(elements, start, k):
            if k == 0:
                result.append(elements[:])
                return

            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()

        dfs([],1,k)
        return result
    
    
    
# solution 3( mine ) - 인덱스로 접근 + start 증가하면서 앞부분 제외 : 1040ms

    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i+1 for i in range(n)]
        result = []

        def combination(sub_list, index):
            if len(sub_list) == k:
                result.append(sub_list[:])
                return

            for i in range(index, n):
                sub_list.append(nums[i])
                combination(sub_list, i+1)
                sub_list.pop()

        combination([],0)
        return result
        
