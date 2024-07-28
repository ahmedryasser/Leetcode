class Solution:
    def arrayNesting(self, nums):
        res = 0
        for i in range(len(nums)):
            if nums[i] != float('inf'):
                start = nums[i]
                count = 0
                while nums[start] != float('inf'):
                    temp = start
                    start = nums[start]
                    count += 1
                    nums[temp] = float('inf')
                res = max(res, count)
        return res