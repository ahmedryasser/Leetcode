class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1 for x in range(k)]
        self.head = 0
        self.tail = 0
        self.size = k
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.head%self.size] = value
        self.head = (self.head +1)%self.size
        # print('enqueue',self.queue, self.head, self.tail)
        self.count+=1
        return True
                
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.tail] = -1
        self.tail = (self.tail + 1)%self.size
        # print('dequeue',self.queue)
        self.count-=1
        return True

    def Front(self) -> int:
        return self.queue[self.tail]

    def Rear(self) -> int:
        # print('rear', self.queue, self.head, self.tail)
        return self.queue[(self.head - 1 + self.size) % self.size]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.size == self.count


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()