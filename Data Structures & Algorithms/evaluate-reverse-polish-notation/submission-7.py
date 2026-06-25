class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque()
        total = 0
        num1, num2 = 0, 0

        for op in tokens:
            if op .isdigit():
                stack.append(int(op))
            else:
                if op == "+":
                    num1, num2 = stack.pop(), stack.pop()
                    total = num1 + num2
                    stack.append(total)
                elif op == "-":
                    num1, num2 = stack.pop(), stack.pop()
                    total = num2 - num1
                    stack.append(total)
                elif op == "*":
                    num1, num2 = stack.pop(), stack.pop()
                    total = num1 * num2
                    stack.append(total)
                elif op == "/":
                    num1, num2 = stack.pop(), stack.pop()
                    total = int(num2 / num1)
                    stack.append(total)
                else:
                    stack.append(int(op))
        return stack.pop()
