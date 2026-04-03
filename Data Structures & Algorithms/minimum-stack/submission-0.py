class MinStack:
    '''
    Ideas:
    1. Minheap / priority queue + stack
        - Pros: all ops natively supported
        - Cons: not all are O(1) time b/c pop requires re-heaping
    '''
    def __init__(self):
        self.stack = []
        self.minPrefix = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.minPrefix.append(val) 
        else:
            # use the minimum value you've seen thus far
            self.minPrefix.append(min(val, self.minPrefix[-1]))
        self.stack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minPrefix.pop()

    def top(self) -> int:
        return self.stack[-1] 

    def getMin(self) -> int:
        return self.minPrefix[-1]
        
