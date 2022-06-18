class Solution:
    def firstUniqChar(self, s: str) -> int:
        i=0
        nStr=s
        while i<len(s):
            if (s[i] not in nStr[i+1:]) and (s[i] not in nStr[:i]):
                return i
            i+=1
        return -1