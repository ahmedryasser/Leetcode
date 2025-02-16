class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%= len(nums)
        copy = nums.copy()
        for i in range(len(nums)):
            nums[i] = copy[((i-k)%len(nums))]

        