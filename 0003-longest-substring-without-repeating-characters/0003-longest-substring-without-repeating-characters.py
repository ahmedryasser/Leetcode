class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        vals = {}
        top = 0
        for r,ch in enumerate(s):
            if ch in vals:
                l = max(l, vals[ch]+1)
            top = max(top, r-l+1)
            vals[ch] = r
            
        return top
