# https://leetcode.com/problems/merge-k-sorted-lists/
'''
- k 개의 정렬된 리스트 하나로 합치면서 정렬하기

- 리스트 별로 heap 에 저장.
- 리스트 별 0번째 원소로 정렬(heappush)하면서 heappop()해서 연결
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        root = result = ListNode(None)
        
        heap = []
        ''' 중복되는 루트 값 push 불가능
        for lst in lists:
            heapq.heappush(heap, (lst.val, lst))
        '''  
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i,lists[i]))
        
        #####
        # next 있으면 다시 heappush ~ push 하면서 재정렬
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]
            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))
            
        return root.next
