class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total_left = 0
        total_right = sum(nums)
        res = []
        for num in nums:
            total_right -=num
            res.append(abs(total_right-total_left))
            total_left +=num
        return res
        