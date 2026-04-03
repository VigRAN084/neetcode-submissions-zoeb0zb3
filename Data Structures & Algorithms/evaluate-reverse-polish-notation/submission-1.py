class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        def operate(operation: str, i1: int, i2: int):
            if operation == '+': return i1 + i2
            elif operation == '-': return i1 - i2
            elif operation == '*': return i1 * i2
            else: return i1 / i2

        for c in tokens:
            if c in operators:
                i2 = int(stack.pop())
                i1 = int(stack.pop())
                res = operate(c, i1, i2)
                stack.append(res)
            else:
                stack.append(c)
        return int(stack[0])

'''
c = '1'
stack = ['1']

c = '2'
stack = ['1', '2']

c = '+'
i1 = 1
i2 = 2
res = 3
stack = [3]

'''



