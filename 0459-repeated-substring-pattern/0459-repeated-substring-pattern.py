class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        for i in range(1,length//2 +1):
            multiple = (length//i)*s[:i]
            if s == multiple:
                return True
        return False