# 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merged = ListNode()
        cur_merged = merged

        left,right = l1,l2
        
        if l1==None and l2 == None:
            return None
        
        while left is not None and right is not None:
            if left.val < right.val:
                cur_merged.val, cur_merged.next = left.val, ListNode()        
                left = left.next
                
            else:
                cur_merged.val, cur_merged.next = right.val, ListNode()
                right = right.next
            
            cur_merged = cur_merged.next
            
        if left != None: # l1 이 안 끝났을 때
            while left.next is not None:
                cur_merged.val, cur_merged.next = left.val, ListNode()
                left = left.next
                cur_merged = cur_merged.next
            cur_merged.val = left.val
        
        if right != None:
            while right.next is not None:
                cur_merged.val, cur_merged.next = right.val, ListNode()
                right = right.next
                cur_merged = cur_merged.next
            cur_merged.val = right.val
            
        return merged



'''
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        l1,l2 = l2, l1
    if l1:
        l1.next = self.mergeTwoLists(l1.next, l2)
    return l1
'''
