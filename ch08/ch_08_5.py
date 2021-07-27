
# https://leetcode.com/problems/swap-nodes-in-pairs/
'''
노드 간 next 바꾸는 순서 + 다음 순서로 넘어갈 때 prev 활용
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
    
        root = prev = ListNode(None)
        node = head
        prev.next = node
        
        while node and node.next:
            
            nextNode = node.next
            
            node.next = nextNode.next
            nextNode.next = node
            
            prev.next = nextNode
            
            node = node.next
            prev = prev.next.next

        return root.next
        
        
        ''' 두 개씩 나눠서...두 번 째 부분 예외처리 x
        while node:
            idx = 0
            
            while idx <2:
                if idx % 2 == 0:
                    print('node',node.val)
                    prev = node
                    nextNode = node.next
                    if nextNode.next != None:
                        node.next = node.next.next.next 
                    else:
                        print('out')
                    print(node.next.val)
                else:
                    node = nextNode.next
                    nextNode.next = prev
                    
                idx += 1 
        '''                   
