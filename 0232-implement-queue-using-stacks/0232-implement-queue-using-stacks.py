class MyQueue:

    def __init__(self):
        self.main_stack = []
        self.second_stack = []

    def push(self, x: int) -> None:
        self.main_stack.append(x)
        print('push',self.main_stack)


    def pop(self) -> int:
        if not self.main_stack:
            return -1
        for _ in range(len(self.main_stack)-1):
            self.second_stack.append( self.main_stack.pop())
        val = self.main_stack.pop()
        while self.second_stack:
            self.main_stack.append(self.second_stack.pop())
        # print(self.main_stack , self.second_stack, val)
        return val

    def peek(self) -> int:
        return self.main_stack[0]

    def empty(self) -> bool:
        return not self.main_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()