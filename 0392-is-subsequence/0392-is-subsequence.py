class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True
        j=0
        for i in t:
            if j>=len(s):
                continue
            elif i==s[j]:
                j+=1
        return j==len(s)