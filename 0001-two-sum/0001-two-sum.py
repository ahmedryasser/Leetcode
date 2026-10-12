class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        vals = {}
        for i, num in enumerate(nums):
            if num in vals:
                return [vals[num],i]
            vals[target-num] = i
        return -1