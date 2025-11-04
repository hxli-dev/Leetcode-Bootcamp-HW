class MyQueue:

    def __init__(self):
        # 用 list 模拟栈：append = push, pop() = pop from top
        self.inStack = []   # 负责 push
        self.outStack = []  # 负责 pop / peek

    def push(self, x: int) -> None:
        # 直接压到 inStack
        self.inStack.append(x)

    def _move(self):
        """当 outStack 为空时，把 inStack 的元素全部倒过去"""
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())

    def pop(self) -> int:
        # 确保 outStack 里有当前队头
        self._move()
        return self.outStack.pop()

    def peek(self) -> int:
        # 同样先移动，再看栈顶就是队头
        self._move()
        return self.outStack[-1]

    def empty(self) -> bool:
        # 两个栈都空才是空队列
        return not self.inStack and not self.outStack
