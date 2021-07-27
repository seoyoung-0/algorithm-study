# https://leetcode.com/problems/add-two-numbers/
'''
연결리스트 역순 + 리스트와 연결리스트 간 변환 
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def reverseList(head:ListNode): # 연결 리스트 reverse 
        
            node, prev = head, None

            while node:
                next_node, node.next = node.next, prev
                prev, node = node, next_node

            return prev
        
        def toList(head:ListNode): # 연결리스트 to 리스트
            li = []
            while head:
                li.append(head.val)
                head = head.next
                
            return li
        
        def toLinkedList(result:List): # 리스트 to 연결리스트
            
            head = ListNode(result[0])
            nextNode = head

            for i in range(1,len(result)):
                nextNode.next = ListNode(result[i])
                nextNode = nextNode.next

            return head
                
                      
        l1 = toList(reverseList(l1))
        l2 = toList(reverseList(l2))
        print(l1,l2)
        
    
        num1 = int(''.join(str(e) for e in l1))
        # num1 = int(''.join(map(str, l1)))
        
        num2 = int(''.join(str(e) for e in l2))
        res = num1 + num2
        print(res)
        
        result = [int(n) for n in str(res)]
        result.reverse()
        
        node = toLinkedList(result)
        return node

        
