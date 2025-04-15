class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        freq = {}
        l = r = 0
        res =0
        for r in range(len(nums)):
            freq[nums[r]] = freq.get(nums[r],0) +1

            while max(freq)- min(freq) >2:
                freq[nums[l]] -=1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l+=1

            res += r-l+1

        return res