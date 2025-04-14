class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        res = 0
        l = 0
        maxF = 0
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r],0) + 1
            maxF = max(counts[s[r]], maxF)
            while (r-l+1) - maxF > k and l<r:
                counts[s[l]] -=1
                l+=1
            res = max(res, r-l+1)
        return res