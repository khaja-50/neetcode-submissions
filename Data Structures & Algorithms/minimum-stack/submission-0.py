class MinStack:

    def __init__(self):
        self.g=[]
    def push(self, val: int) -> None:
        self.g.append(val)
    def pop(self) -> None:
        self.g.pop()
    def top(self) -> int:
        return self.g[-1]
    def getMin(self) -> int:
        return min(self.g)
        
