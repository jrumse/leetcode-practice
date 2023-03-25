class MyQueue:

    inStack = list()
    outStack = list()

    def __init__(self):
        self.inStack = []
        self.outStack = []
        

    def push(self, x: int) -> None:
        self.inStack.append(x)
        

    def pop(self) -> int:
        # Place Contents in the in stack into the out stack
        # [ x , y , z ] -> [ z , y , x ]
        while self.inStack:
            self.outStack.append(self.inStack.pop())
    
        # Pop front (return x) -> [ z , y ]
        returnVal = self.outStack.pop()
        
        # Place contents in the out stack into the in stack
        # [ z , y ] -> [ y , z ]
        while self.outStack:
            self.inStack.append(self.outStack.pop())

        return returnVal
        

    def peek(self) -> int:

        while self.inStack:
            self.outStack.append(self.inStack.pop())
        
        returnVal = self.outStack.pop()
        self.inStack.append(returnVal)

        while self.outStack:
            self.inStack.append(self.outStack.pop())
        
        return returnVal


    def empty(self) -> bool:
        return len(self.inStack) == 0