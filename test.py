#pylint: disable=no-member
import expression
import reverse
import homeade_stack

swap = reverse.Reverse()
tool = expression.Expression('(len)<dskfjlksdf[slfkjdsf]>')
stack = homeade_stack.stack()


stack.push(5)
stack.push(2)
stack.push(14)
stack.push(33)
stack.pop()
stack.pop()


stack.print()
print(stack.is_empty())
