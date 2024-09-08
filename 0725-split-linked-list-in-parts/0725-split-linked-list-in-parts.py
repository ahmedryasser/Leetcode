# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size = getSize(head)
        min_len, one_more = divmod(size, k)
        res = []
        current = ListNode(None)
        current.next = head
        
        for i in range(k):
            ans = current
            for _ in range(min_len + int(i<one_more)):
                current = current.next
            res.append(ans.next)
            ans.next = None
        return res
        
        
        
def getSize(head: ListNode):
    length = 0
    while head:
        head = head.next
        length +=1
    return length