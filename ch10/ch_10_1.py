# https://leetcode.com/problems/design-circular-deque/
'''
- insert 할 때 앞 뒤 다 이어주기 주의 
'''
class Node:
    def __init__(self, value, right_node=None, left_node=None):
        self.value = value
        self.right = right_node
        self.left = left_node

class MyCircularDeque:

    def __init__(self, k: int):
        
        self.size = k
        self.len = 0
        self.head, self.tail = Node(None), Node(None)
        self.head.right, self.tail.left = self.tail, self.head
        
    def insertFront(self, value: int) -> bool:

        if self.len == self.size:
            return False
        node = Node(None)
        node.value = value
        
        node.right = self.head.right
        self.head.right.left = node
        
        self.head.right = node
        node.left = self.head
        
        self.len += 1
        return True

    def insertLast(self, value: int) -> bool:

        if self.len == self.size:
            return False
        node = Node(None)
        node.value = value
        
        self.tail.left.right = node
        node.left = self.tail.left
        
        self.tail.left = node
        node.right = self.tail
        
        self.len += 1
        return True
    
    def deleteFront(self) -> bool:

        if self.len == 0 :
            return False
        
        nextNode = self.head.right.right # 다음 첫 번째 
        v = self.head.right.value
        
        self.head.right = nextNode
        nextNode.left = self.head
        
        self.len -=1
        return True

    def deleteLast(self) -> bool:

        if self.len == 0 :
            return False
        prevNode = self.tail.left.left
        v = self.tail.left.value
        
        self.tail.left = prevNode
        prevNode.right = self.tail
        
        self.len -= 1
        return True
        

    def getFront(self) -> int:
        
        if self.len == 0:
            return -1
        return self.head.right.value
        

    def getRear(self) -> int:

        if self.len == 0:
            return -1
        return self.tail.left.value
        

    def isEmpty(self) -> bool:

        return self.len == 0
        

    def isFull(self) -> bool:

        return self.len == self.size
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
