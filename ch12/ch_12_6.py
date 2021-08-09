# https://leetcode.com/problems/subsets/
'''
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

- dfs 트리에서 발생하는 모든 sublist(path) 다 추가하기
'''
class Solution:

# solution 1 (mine) - 36ms
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(start, sub):
            result.append(sub[:])
            for i in range(start, len(nums)):
                sub.append(nums[i])
                dfs(i+1, sub)
                sub.pop()

        dfs(0,[])
        return result
    
    
    
# solution 2 - 32ms    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        def dfs(index, path):
            result.append(path[:])
            
            for i in range(index, len(nums)):
                dfs(i+1, path + [nums[i]])
                
        dfs(0,[])       
        return result
        
