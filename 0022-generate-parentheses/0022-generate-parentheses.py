class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []
        
        def backtrack(openPar, closedPar):
            
            if openPar == closedPar == n:
                result.append("".join(stack))
                return
            
            if openPar < n:
                stack.append("(")
                backtrack(openPar+1, closedPar)
                stack.pop()
                
            if openPar > closedPar:
                stack.append(")")
                backtrack(openPar, closedPar+1)
                stack.pop()
                
        backtrack(0,0)
        return result