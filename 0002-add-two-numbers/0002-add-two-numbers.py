# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head  = l1
        val1 = []
        while head != None:
            val1.append(str(head.val))
            head = head.next
        val2 = []
        head  = l2
        while head != None:
            val2.append(str(head.val))
            head = head.next

        final_val = int(''.join(val1[::-1]) if val1 != [] else 0) + int(''.join(val2[::-1])if val2 != [] else 0)
        result_list = list(str(final_val))[::-1]
        node = ListNode(0)
        head =node
        for res in result_list:
            head.next = ListNode(0)  
            head = head.next
            head.val = int(res)
            
        
        return node.next
