class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order = [*order]
        s = [*s]
        fStr = ""
        for i in order:
            while i in s:
                s.remove(i)
                fStr += i    
        newStr = "".join(s)
        return fStr + newStr