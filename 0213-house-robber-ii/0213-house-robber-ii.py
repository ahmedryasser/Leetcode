class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        max_sum1 = nums[:-1].copy()
        print(max_sum1)
        max_sum1[1] = max(nums[1], nums[0])
        for i in range(2,len(max_sum1)):
            max_sum1[i] = max(max_sum1[i-1], max_sum1[i-2] + nums[i])
        print(max_sum1)
        max_sum2 = nums[1:].copy()
        print(max_sum2)
        max_sum2[1] = max(nums[2], nums[1])
        for i in range(2,len(max_sum2)):
            max_sum2[i] = max(max_sum2[i-1], max_sum2[i-2] + nums[i+1])
        print(max_sum2)
        return max(max_sum1[-1], max_sum2[-1])

        
