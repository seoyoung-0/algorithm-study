# https://leetcode.com/problems/palindrome-linked-list/
'''
연결 리스트가 팰린드롬 구조인지 판별하라
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# sol1. 리스트로 변환 - 팰린드롬은 pop 으로
# 1404 ms
def isPalindrome(head: ListNode) -> bool:
    h_list = []
    node = head
    while node is not None:
        h_list.append(node.val)
        node = node.next

    while len(h_list)>1:
        if h_list.pop(0) != h_list.pop():
            return False

    return True

# sol2. 연결리스트 자체에서 해결 - deque 로 앞뒤 pop
# 832 ms
from collections import deque

def isPalindrome2(head : ListNode)->bool:
    
    deq = deque()
    
    node = head
    
    while node is not None:
        deq.append(node.val)
        node = node.next
        
    while len(deq)>1:
        if deq.popleft() != deq.pop():
            return False
    
    return True


if __name__=="__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(2)
    node4 = ListNode(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    print(isPalindrome(head))
    print(isPalindrome2(head))
