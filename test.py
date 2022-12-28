#pylint: disable=no-member
import expression
import reverse
import homeade_stack
import double_stack
import min_stack

swap = reverse.Reverse()
tool = expression.Expression('(len)<dskfjlksdf[slfkjdsf]>')
stack = homeade_stack.stack()
double = double_stack.Double_Stack()
minStack = min_stack.Min_Stack(10)

minStack.push(3)
minStack.push(4)
minStack.push(5)

minStack.print()

minStack.pop()

minStack.print()

print(minStack.min())