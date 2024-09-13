# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next or left == right:
            return head
        start = head
        if left > 1: prev = head
        for _ in range(left-1):
            prev = start
            start = start.next
        end = head
        for _ in range(right-1):
            end = end.next
        if left > 1 and prev: prev.next = None
        after, end.next = end.next, None if end else None
            
        before, curr = None, start
        while curr is not None:
            temp = before
            before, curr.next, curr = curr, before, curr.next
        if left>1 :
            prev.next = before
        else:
            head = before
        start.next = after
        
        return head
        