from functools import lru_cache
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l = 0 
        r = len(colors)-1
        val = [0]
        @lru_cache
        def attempt(l,r):
            if l == r:
                return
            if colors[l] != colors[r]:
                val[0] = max(val[0], abs(l-r))
            attempt(l+1, r)
            attempt(l,r-1)
        attempt(l,r)
        return val[0]
            