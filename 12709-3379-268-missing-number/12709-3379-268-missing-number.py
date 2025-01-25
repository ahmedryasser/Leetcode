class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numbers = set(nums)
        for i in range(len(nums)):
            if i not in numbers:
                return i
        # Replace this placeholder return statement with your code
        return i+1