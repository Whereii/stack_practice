#This class contains a method which checks to see if a string is properly formatted or not

class Expression:
    def __init__(self, val):
        self.val = val
        self.left_bracket = ['{', '[', '<', '(']
        self.right_bracket = ['}', ']', '>', ')']
    
    def check(self):
        stack = []
        for i in self.val:
            if self.is_left_bracket(i):
                stack.append(i)
            
            if self.is_right_bracket(i):
                if not stack:
                    return 'Your string is improperly formatted'

                top_value = stack.pop()
                if self.is_match(top_value, i):
                    continue
                else:
                    return 'Your string is improperly formatted'

        if not stack:
            return 'Your string is correct'
        else:
            return 'Your string is improperly formatted'

    def is_left_bracket(self, val):
        return val in self.left_bracket

    def is_right_bracket(self, val):
        return val in self.right_bracket

    def is_match(self, left, right):
        left_index = self.left_bracket.index(left)
        right_index = self.right_bracket.index(right)
        return left_index == right_index