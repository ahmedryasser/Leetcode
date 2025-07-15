class Solution:
    def countAsterisks(self, s: str) -> int:
        cnt = 0
        i = 0
        while i < len(s):
            if s[i] == "*":
                cnt +=1
            elif s[i] == "|":
                i+=1
                while i<len(s) and s[i] != "|":
                    i+=1
            i+=1
        return cnt
        