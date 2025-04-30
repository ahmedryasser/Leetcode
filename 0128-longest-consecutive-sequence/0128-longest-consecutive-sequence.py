class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        for num in nums:
            streak = 1
            if num-1 not in num_set:
                current = num
            
            while num+1 in num_set:
                num+=1
                streak+=1

            longest = max(streak,longest)
        
        return longest
            
