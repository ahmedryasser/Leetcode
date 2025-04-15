class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        freq = {0:0,1:0}
        res = 0
        for r in range(len(nums)):
            freq[nums[r]] += 1

            while freq[0]>k:
                freq[nums[l]] -=1
                l+=1

            res = max(res, r-l+1)
        return res
