class MinStack:

    def __init__(self):
        self.s = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if len(self.minStack) > 0 and self.minStack[-1] >= val:
            self.minStack.append(val)
        elif len(self.minStack) == 0:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.s[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
