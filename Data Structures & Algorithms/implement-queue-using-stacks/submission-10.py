class MyQueue:

    def __init__(self):
        self.r=[]
        self.z=[]
    def push(self, x: int) -> None:
        self.r.append(x)
    def rev(self):
            if not self.z:
                while self.r:
                    self.z.append(self.r.pop())
    def pop(self) -> int:
    
        self.rev()
        return self.z.pop()
    def peek(self) -> int:
        self.rev()
        return self.z[-1]
    def empty(self) -> bool:
        return len(self.r)==0 and len(self.z)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()