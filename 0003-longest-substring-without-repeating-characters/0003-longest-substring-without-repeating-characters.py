class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=0
        if s == "": return 0
        b=1
        top = 1
        arr = list(s)
        length = len(arr)
        vals = {}
        while b < length:
            vals[arr[a]] = 1
            curr = 1
            while b < len(arr) and arr[b] not in vals:
                curr+=1
                vals[arr[b]] = 1
                b+=1
            top = max(curr, top)
            vals = {}
            a+=1
            b=a+1
        return top