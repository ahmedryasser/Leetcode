class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        count =0
        for char in s:
            if char == "[": stack.append(char)
            else:
                if not stack:
                    stack.append(char)
                    count+=1
                else:
                    stack.pop()
        return count