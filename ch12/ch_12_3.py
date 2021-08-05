# https://leetcode.com/problems/permutations/
'''
* 순열 경우의 수 출력
- 남은 숫자 리스트 갱신하고, sub list 갱신하면서 dfs 재귀 
[1,2,3] - [1,3,2] - [2,1,3] ...순으로 저장
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        
        return list(permutations(nums))
        
        
    ''' 
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        sub =[]
        
        def dfs(sub_list, remain_list):

            if len(sub_list) == len(nums):
                result.append(sub_list[:]) 
                
                # sub_list 말고 sub_list[:] 로 추가해줘야 result 에 담긴다..
                # 객체 복사의 차이
                # -  [:]로 저장할 경우, 복사해서 다른 id 를 갖는 새로운 객체를 저장
                # - 그냥 sub_list로 저장할 경우, 참조 복사라서 바뀌면 같이 바뀌어 버림
                
                return
            else:
                for n in remain_list:
                    prev = remain_list[:]
                    sub.append(n)
                    prev.remove(n)
                    dfs(sub,prev)
                    sub.pop()
        
        dfs(sub, nums)
        return result
        '''
        
