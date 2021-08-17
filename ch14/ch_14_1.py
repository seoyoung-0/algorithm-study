# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''
Input: root = [3,9,20,null,null,15,7]
Output: 3

- BFS 로, depth 같은 거 모두 탐색, 자식있으면 지금 큐에 넣기
- for 문으로 queue 돌아도 queue 는 자식으로 다시 구성
- -> 다음 queue 는 depth 증가된 자식 노드로 구성 
'''
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        queue = deque([root])
        depth = 0 
        
        while queue:
            depth += 1
            
            for i in range(len(queue)):

                cur = queue.popleft()
                
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return depth
        
