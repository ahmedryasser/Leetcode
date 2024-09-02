class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j=0
        for push in pushed:
            stack.append(push)
            while stack and popped[j] == stack[-1]:
                stack.pop()
                j+=1
        return j == len(popped)
            