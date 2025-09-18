import numpy as np

class Stack:
    def __init__(self):
        self.top = -1
        self.elem = np.zeros(50, dtype=int)

    def push(self, _n):
        if type(_n) == int:
            self.top += 1
            self.elem[self.top] = _n

    def pop(self):
        if self.top < 0:
            return None
        n = self.elem[self.top]
        self.top -= 1
        return n
    
    def isEmpty(self):
        return self.top < 0
    
    def dump(self):
        text = ""
        for i in range(self.top, -1, -1):
            text += f"{self.elem[i]}\n"
        return text