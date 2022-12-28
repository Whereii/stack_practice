import array as arr

class stack:
    def __init__(self):
        self.array = arr.array('i', [])

    def push(self, value):
        self.array.insert(0, value)

    def pop(self):
        self.array.pop(0)

    def print(self):
        full_arry = []
        for i in self.array:
            full_arry.append(i)
        print(full_arry)

    def peek(self):
        if not self.array:
            raise Exception('emptyArray')
        return self.array[0]

    def is_empty(self):
        if not self.array:
            return True
        else:
            return False
        