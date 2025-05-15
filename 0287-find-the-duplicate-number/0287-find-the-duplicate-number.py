class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        vals = {}
        for num in nums:
            if num in vals: return num
            vals[num] = 1
        
