# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
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
        curr = head
        mid = prev
        while mid:
            if curr.val != mid.val:
                return False
            curr,mid = curr.next,mid.next
            
        return True
        