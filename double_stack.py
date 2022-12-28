class Double_Stack:
    def __init__(self):
        self.stack = []
        self.counter_one = 0
        self.counter_two = 1

    def push1(self, val):
        while len(self.stack) <= self.counter_one:
            self.stack.append(0)
        self.stack[self.counter_one] = val
        self.counter_one += 2
    
    def push2(self, val):
        while len(self.stack) <= self.counter_two:
            self.stack.append(0)
        self.stack[self.counter_two] = val
        self.counter_two += 2

    def print1(self):
        array_one = []
        if self.counter_one == 0:
            raise Exception('invalidStateException')
        for i in range(0, (self.counter_one), 2):
            array_one.append(self.stack[i])
        print(array_one)
    
    def print2(self):
        array_two = []
        if self.counter_two == 0:
            raise Exception('invalidStateException')
        for i in range(1, self.counter_two, 2):
            array_two.append(self.stack[i])
        print(array_two)

    def pop1(self):
        if self.counter_one == 0:
            raise Exception('invalidStateException')
        self.stack[self.counter_one - 2] = 0
        self.counter_one = self.counter_one - 2

    def pop2(self):
        if self.counter_two == 1:
            raise Exception('invalidStateException')
        self.stack[self.counter_two - 2] = 0
        self.counter_two = self.counter_two - 2

    def is_empty1(self):
        return self.counter_one == 0
    
    def is_empty2(self):
        return self.counter_two == 1