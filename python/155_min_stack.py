class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def __repr__(self):
        return str(self.stack)

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min[-1] if self.min else val)
        self.min.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# test
minstack = MinStack() 

minstack.push(-2)
print(minstack == [-2])
minstack.push(0)
minstack.push(-3)
print(minstack)
print(minstack.getMin())
minstack.pop()
print(minstack)
print(minstack.top())
print(minstack)
print(minstack.getMin())
print(minstack)