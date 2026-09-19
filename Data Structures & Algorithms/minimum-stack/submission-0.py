class MinStack:

    def __init__(self):
        self.stack = []
        self.minSoFar = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minSoFar):
            self.minSoFar.append(min(val, self.minSoFar[len(self.minSoFar)-1]))  
        else:
            self.minSoFar.append(val)
        return None

    def pop(self) -> None:
        self.stack.pop()
        self.minSoFar.pop()
        return None
        

    def top(self) -> int:
        top = None
        if len(self.stack):
            top = self.stack[len(self.stack)-1]
        return top
        
    def getMin(self) -> int:
        return self.minSoFar[len(self.minSoFar)-1]
        


        
