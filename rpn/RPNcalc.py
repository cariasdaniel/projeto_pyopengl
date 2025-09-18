from stack import *

class RPNcalc:
    def __init__(self):
        self.stack = Stack()

    def getOperands(self):
        if self.stack.isEmpty():
            raise IndexError("Empty stack!\n")
        
        n1 = self.stack.pop()
        if self.stack.isEmpty():
            self.stack.push(n1)
            raise IndexError("Two operands needed!\n")
        
        n2 = self.stack.pop()
        return int(n1), int(n2)
    
    def enterNumber(self, _n):
        self.stack.push(_n)

    def selectOp_sum(self):
        n1, n2 = self.getOperands()
        ans = n2+n1
        self.stack.push(ans)
        return ans
        
    def selectOp_diff(self):
        n1, n2 = self.getOperands()
        ans = n2-n1
        self.stack.push(ans)
        return ans

    def selectOp_prod(self):
        n1, n2 = self.getOperands()
        ans = n2*n1
        self.stack.push(ans)
        return ans

    def selectOp_div(self):
        n1, n2 = self.getOperands()
        if n1 != 0:
            ans = n2//n1
            self.stack.push(ans)
            return ans, n2%n1
        else:
            raise ValueError("Division by zero is not allowed!\n")

    def clearStack(self):
        self.stack = Stack()