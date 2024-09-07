# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return True
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        curr, prev = slow,None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        slow.next, first,second = None, head, prev
        while second and second.next:
            temp1, temp2 = first.next, second.next
            first.next= second
            second.next = temp1
            first,second = temp1,temp2
        return head