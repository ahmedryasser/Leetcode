class Solution:
    def minLength(self, s: str) -> int:
        while "AB" in s or "CD" in s:
            if "AB" in s:
                s = "".join(s.split("AB"))
            if "CD" in s:
                s = "".join(s.split("CD"))
        return len(s)