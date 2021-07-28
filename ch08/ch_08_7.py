# https://leetcode.com/problems/reverse-linked-list-ii/
'''
* 지정된 구간만 reverse 연결 리스트로 바꾸기
- start 와 end 로 구간 지정 
- 구간지정 외에 temp 지정 : start 와 end 사이의 노드로 연결할 때 사용
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        
        if head is None or left == right:
            return head
        
        root = ListNode(None)
        root.next = head
        
        start, end = root, root.next
        for _ in range(left-1): # 시자 구간과 end 지정
            start = start.next
        end = start.next
        
        for _ in range(right - left):
            temp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = temp
            
        return root.next
            
        
        
