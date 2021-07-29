# https://leetcode.com/problems/design-circular-queue/
'''
리스트, front, rear 존재하는 원형 큐 
- front 랑 rear 함수 문제가 요구하는 리턴 값 확인하기
'''
class MyCircularQueue:

    def __init__(self, k: int):
        
        self.queue = [None]*k
        self.front = self.rear = 0 

    def enQueue(self, value: int) -> bool:
        if self.queue[self.rear] is None:
            self.queue[self.rear] = value
            self.rear = (self.rear + 1 ) % len(self.queue)
            return True
        else:
            return False
        
    def deQueue(self) -> bool:
        
        if self.queue[self.front] is not None: # 값이 있으면
            self.queue[self.front] = None
            self.front = (self.front+1) % len(self.queue)
            return True
        else:
            return False

    def Front(self) -> int:
        # 큐 비어있으면 -1, 아니면 첫번째 item 리턴
        if self.queue[self.front] is None:
            return -1
        else:
            return self.queue[self.front]

    def Rear(self) -> int:
        # 큐 비어있으면 -1, 아니면 마지막 item 리턴 
        print(self.rear)
        if self.queue[self.rear-1] is None:
            return -1
        else:
            return self.queue[self.rear-1]

    def isEmpty(self) -> bool:
        
        return self.queue[self.front] is None # 72ms 
        
        # return self.front == self.rear and elf.queue[self.front] is None # 64ms

    def isFull(self) -> bool:
        
        return self.queue[self.rear] is not None
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
