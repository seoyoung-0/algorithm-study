# https://leetcode.com/problems/reverse-linked-list/
'''
연결리스트 뒤집기
- 뒤로 진행하면서, 동시에 prev 를 next 로 연결해주기
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        
        node, prev = head, None
    
        while node:
            next_node, node.next = node.next, prev
            prev, node = node, next_node

        return prev
        
        ''' 재귀함수
        def reverse(self, node: ListNode, prev: ListNode=None):
            
            if not node:
                return prev
            next_node, node.next = node.next, prev
            print(prev.val)
            return reverse(next_node, node)
        
        return reverse(head,None)
        '''
        
        



    
