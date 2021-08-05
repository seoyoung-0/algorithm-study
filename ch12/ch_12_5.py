# https://leetcode.com/problems/combination-sum/
'''
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

- 순열, 조합 종합?해서 풀었다.
- remain_list 에서 자기 뒤쪽 것만 보내주고
- pop 할 때는 해당 숫자는 sum 에서도 빼주기
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(sum,path,remain_list):

            if sum == target:
                result.append(path[:])
                return 
            
            if sum > target:
                return 

            else:
                for i,n in enumerate(remain_list):  
                    sum += n
                    path.append(n)
                    dfs(sum,path,remain_list[i:])
                    sum -= path.pop()

        dfs(0,[],candidates)
        return result
        
