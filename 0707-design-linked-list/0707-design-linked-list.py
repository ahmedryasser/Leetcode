# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length: return -1
        node = self.head
        for _ in range(index+1):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length, val)
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return 
        if index < 0:
            index = 0

        node = self.head
        for _ in range(index):
            node = node.next
        new = ListNode(val)
        new.next = node.next
        node.next = new
        self.length+=1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length or index <0:
            return 
        if index < 0:
            index = 0

        node = self.head
        for _ in range(index):
            node = node.next
        
        node.next = node.next.next
        self.length-=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList(
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)