class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        val = float('inf')
        for i,num in enumerate(nums):
            if target == nums[i]:
                val = min(val, abs(i-start))
        return val