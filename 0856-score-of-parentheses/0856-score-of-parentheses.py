class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        score = 0
        for char in s:
            if char == "(" :
                stack.append(0)
            else:
                val = stack.pop()
                val = max( 1,val*2)
                stack[-1] += val
                
        return stack.pop()
                
                