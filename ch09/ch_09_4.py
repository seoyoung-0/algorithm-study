# https://leetcode.com/problems/implement-stack-using-queues/


from collections import deque

class MyStack:

    def __init__(self):

        self.queue = deque()
        
    def push(self, x: int) -> None:
        
        queue = self.queue 
        queue.append(x)
        for i in range(len(queue)-1):
            queue.append(queue.popleft())
        
    def pop(self) -> int:
        
        return self.queue.popleft()
        
    def top(self) -> int:
        
        return self.queue[0]

    def empty(self) -> bool:
        if self.queue:
            return False
        else:
            return True
        # return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
