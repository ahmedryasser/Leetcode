# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        highest = 0
        length = 0
        start = head
        values =[]
        while start:
            values.append(start.val)
            start = start.next
        while values:
            top, bottom = values.pop(0), values.pop(len(values)-1)
            highest = max(highest, top+bottom)
        return highest
        