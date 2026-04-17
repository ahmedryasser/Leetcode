class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        seen = {}
        ans = float("inf")

        for i, num in enumerate(nums):               
            if num in seen:
                ans = min(ans, i - seen[num])
            rev = int(str(num)[::-1])
            seen[rev] = i
            
        return -1 if ans == float('inf') else ans