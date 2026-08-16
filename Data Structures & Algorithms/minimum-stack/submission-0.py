class MinStack:

    def __init__(self):
        self.stack = [] 

    def push(self, val: int) -> None:
        if len(self.stack) == 0 : 
            self.stack.append([val,val])
        else: 
            cur_min = self.stack[-1][1] 
            mini = min(cur_min, val) 
            self.stack.append([val, mini]) 

    def pop(self) -> None:
        if self.stack: 
            self.stack.pop() 

    def top(self) -> int:
        if not self.stack: 
            return None 
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack: 
            return None 
        return self.stack[-1][1] 
