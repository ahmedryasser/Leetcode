# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return None
#         elif not head.next:
#             return head
#         elif not head.next.next:
#             return None if head.next.val == head.val else head
            
#         prev= head
#         current = head.next
#         then = current.next
#         while then:
#             if prev.val == current.val == then.val:
#                 while then and then.val == current.val:
#                     then = then.next
#                 head = then
#                 prev = then.next if then else None
#                 current = prev.next if prev else None 
#                 then = current.next if current and current.next else None 
#             elif current.val == then.val:
#                 while then and then.val == current.val:
#                     then = then.next
#                 prev.next = then if then else None
#                 current = prev.next if prev.next else None 
#                 then = current.next if current and current.next else None 
#             elif prev.val == current.val:
#                 prev = then if then else None
#                 current = prev.next if prev.next else None 
#                 then = current.next if current and current.next else None 
#             else:
#                 prev = current if current else None
#                 current = prev.next if prev.next else None 
#                 then = current.next if current and current.next else None 
#         return head
        visited = []
        dupe = []
        point = head
        while point:
            if point.val not in visited:
                visited.append(point.val)
            else:
                if point.val not in dupe:
                    dupe.append(point.val)
            point = point.next
        for node in dupe:
            visited.remove(node)
        start = ListNode(0)
        point = start
        for node in visited:
            point.next = ListNode(node)
            point = point.next
            
        return start.next
        