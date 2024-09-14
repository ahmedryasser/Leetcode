# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        if not list1.next:
            return list1
        start = list1
        if a > 0: prev = list1
        for _ in range(a):
            prev = start
            start = start.next
        end = list1
        for _ in range(b):
            end = end.next
        end2 = list2
        prev.next = list2
        while end2.next:
            end2 = end2.next
        end2.next = end.next
            
        
        return list1