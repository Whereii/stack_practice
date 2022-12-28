#The goal of this program is to create a stack that can retrieve the min value -
# in the stack in O(1) time

class Min_Stack:
    def __init__(self, size):
        self.min_num = None
        self.stack = [None] * size
        self.counter = 0

    def push(self, val):
        if self.counter == len(self.stack):
            raise Exception('stackOverflowException')
        self.stack[self.counter] = val
        self.counter += 1
        if self.min_num == None:
            self.min_num = val
        if val < self.min_num:
            self.min_num = val
    
    def pop(self):
        if self.counter == 0:
            raise Exception('invalidStateException')
        self.stack[self.counter - 1] = None
        self.counter -= 1
    
    def min(self):
        return self.min_num
    
    def print(self):
        holder = []
        for i in range(self.counter):
            holder.append(self.stack[i])
        print(holder)