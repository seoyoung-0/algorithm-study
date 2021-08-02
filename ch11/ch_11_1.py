# https://leetcode.com/problems/design-hashmap/

from collections import defaultdict

class ListNode:
    def __init__(self, key=None, value= None):
        self.key = key
        self.value = value
        self.next = None
class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = defaultdict(ListNode)
        
    def put(self, key: int, value: int) -> None:
    # 키, 값을 해시맵에 삽입
    # 존재하는 키라면 값을 업데이트 ( separate chaining)
        index = key % self.size
        
        if self.table[index].value is None:
            self.table[index] = ListNode(key,value)
            return
        
        # 해당 인덱스에 노드가 존재하는 경우 : 해시 충돌 발생
        # 이미 키가 존재할 경우 업데이트 하고 빠져나감
        # next 가 None 인 경우 아무것도 안 하고 빠져나감
        now = self.table[index]
        while now:
            if now.key == key:
                now.value = value
                return
            if now.next is None:
                break
                
            now = now.next
            
        # 체이닝 에 해당 노드 연결
        now.next = ListNode(key,value) 


    def get(self, key: int) -> int:
    # 키에 해당하는 값을 조회, 존재하지 않으면 -1 리턴
        index = key % self.size
        
        if self.table[index].value is None:
            return -1
        
        now = self.table[index]
        while now:
            if now.key == key:
                return now.value
            now = now.next
        return -1 # 탐색하는데 값이 없으면 -1

        
    def remove(self, key: int) -> None:
    # 키에 해당하는 키,값 노드를 해시맵에서 삭제
        index = key % self.size
        
        if self.table[index].value is None:
            return 
        now = self.table[index]
        
        if now.key == key :
            # 1개만 있을 때
            if now.next is None:
                self.table[index] = ListNode()
            else:
                return
            
        now = self.table[index]
        prev = now
        while now:
            if now.key == key:
                prev.next = now.next
                return
            prev, now = now, now.next
        
            
            
"""         
obj = MyHashMap()
obj.put(1,1)
obj.put(2,2)
obj.put(1,2)
param_2 = obj.get(1)
print(param_2)
obj.remove(key)
"""
