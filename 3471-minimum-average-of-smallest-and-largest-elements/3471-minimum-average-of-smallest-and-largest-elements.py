class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        smallest = float('inf')
        nums.sort()
        top,bot = 0, len(nums)-1
        while top<=bot:
            smallest = min(smallest, (nums[top]+nums[bot])/2)
            top+=1
            bot -=1
        return smallest

