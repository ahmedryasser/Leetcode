# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length +=1
        tail.next = head
        moves = length - k%length
        prev = head
        tail = head
        for _ in range(moves-1):
            prev = tail
            tail = tail.next
        new_tail = tail.next
        tail.next = None
        return new_tail
        