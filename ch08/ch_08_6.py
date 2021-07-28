# https://leetcode.com/problems/odd-even-linked-list/
'''
node 가 하나씩 넘어가면 마지막 짝수일 때랑 홀수일 때가 나뉘게 된다.
odd, even 함께 증가하면, 마지막에 odd.next 에 first_even 만 연결해주면 
마지막이 짝수인지 홀수인지 고려할 필요가 없다.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if head is None:
            return None
            
        odd = head
        even = head.next
        first_even = head.next
        
        while even and even.next:
            odd.next , even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        
        odd.next = first_even
        return head
     
        

        '''
        root = ListNode(None)
        
        first_even = head.next
        node = head
        prev = ListNode(None)
        
        while node and node.next:  
            nextNode = node.next
            node.next = nextNode.next
              
            node = nextNode
            
            node.next = first_even
        
        return head
        '''
        
        
            
            
