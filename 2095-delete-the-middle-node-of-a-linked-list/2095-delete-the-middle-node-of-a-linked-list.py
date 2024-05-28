# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None: 
            head = None
            return None
        counter = head
        count = 0
        while counter.next != None:
            count +=1
            counter = counter.next
        middle = head
        prev= head
        for i in range(math.ceil(count/2)):
            prev=middle
            middle = middle.next
        prev.next = middle.next
        return head
            