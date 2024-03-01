# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is not None:
            first = head
            second = head.next
            first.next= None
            while second is not None:
                temp = second.next
                second.next = first
                first = second
                second = temp
            head = first
            return head
        else:
            return head