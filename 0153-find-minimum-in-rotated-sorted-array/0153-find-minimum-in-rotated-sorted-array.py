class Solution:
    def findMin(self, nums: List[int]) -> int:
        prev = -5001
        for num in nums:
            if num < prev:
                return num
            else:
                prev = num
        return nums[0]