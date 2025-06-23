class Solution:
    def reverseDegree(self, s: str) -> int:
        alpha="abcdefghijklmnopqrstuvwxyz"
        vals = {}
        i = 26
        for c in alpha:
            vals[c] = i
            i-=1
        total = 0
        for n,ch in enumerate(s):
            total += vals[ch]*(n+1)

        return total
        