# class Solution:
#     def removeStars(self, s: str) -> str:
#         arr = list(s)
#         i = 1
#         j = 0
#         while i < len(arr):
#             if arr[i] == "*":
#                 arr.pop(i)
#                 arr.pop(j)
#                 if i > 1:
#                     i-=1
#                     j-=1
#             else:
#                 j=i
#                 i+=1
#         return "".join(arr)
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        def push(l):
            stack.append(l)
        def pop():
            return stack.pop()
        arr = list(s)
        for i in arr:
            if i != '*':
                push(i)
            else:
                pop()
        return "".join(stack)
            
        
            