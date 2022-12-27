#This class contains a method which reverses a string utilizing a stack algorithm

class Reverse:
    def __init__(self):
        pass

    def reverse(self, val):
        swap = ''
        stack = []
        for i in val:
            stack.append(i)
        for i in val:
            swap = swap + stack.pop()
        print(swap)