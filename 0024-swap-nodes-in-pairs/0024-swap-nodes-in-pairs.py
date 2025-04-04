# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        if prev: 
            curr = prev.next
        else:
            return None
        temp = None
        while prev:
            if prev and curr:
                if temp:
                    prev.next, curr.next, temp.next = curr.next, prev, curr
                else:
                    prev.next, curr.next = curr.next, prev
                if prev: prev = prev.next
                if not temp: 
                    head = curr
                    temp = curr.next
                else:
                    temp = curr.next
                if prev: curr = prev.next
            else:
                return head
        return head
                    