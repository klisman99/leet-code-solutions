class MinStack:

    def __init__(self):
        self.items: list[int] = []
        self.minStack: list[int] = []

    def push(self, val: int) -> None:
        self.items.append(val)

        if not self.minStack or val <= self.minStack[len(self.minStack) - 1]:
            self.minStack.append(val)

    def pop(self) -> None:
        val = self.items.pop()

        if val == self.minStack[len(self.minStack)- 1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.items[len(self.items)- 1]

    def getMin(self) -> int:
        return self.minStack[len(self.minStack)- 1]
