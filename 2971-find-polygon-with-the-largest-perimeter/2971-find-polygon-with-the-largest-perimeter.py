class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        arr = sorted(nums, reverse=True)
        for i,num in enumerate(arr):
            if num < sum(arr[i+1:]) and len(arr[i:]) >= 3:
                return sum(arr[i:])
        return -1