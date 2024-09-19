class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = [-1 for x in range(k)]
        self.head = 0
        self.tail = 0
        self.size = k
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        # print('enqueue fr',self.queue)
        self.head = (self.head -1)%self.size
        self.queue[self.head] = value
        # print('enqueue fr',self.queue, self.head, self.tail)
        self.count+=1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        # print('enqueue last',self.queue)
        self.queue[self.tail] = value
        self.tail = (self.tail +1 +self.size)%self.size
        # print('enqueue last',self.queue, self.head, self.tail)
        self.count+=1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        # print('dequeue fr',self.queue)
        self.queue[self.head] = -1
        self.head = (self.head + 1 + self.size)%self.size
        # print('dequeue fr',self.queue, self.head, self.tail)
        self.count-=1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        # print('dequeue l',self.queue)
        self.tail = (self.tail - 1)%self.size
        self.queue[self.tail] = -1
        # print('dequeue l',self.queue, self.head, self.tail)
        self.count-=1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head ]        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.tail- 1 + self.size) % self.size]        

    def isEmpty(self) -> bool:
        return self.count == 0


    def isFull(self) -> bool:
        return self.size == self.count



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()