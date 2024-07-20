class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running = 0
        for i,num in enumerate(nums):
            temp = nums[i]
            nums[i] += running
            running += temp
        return nums