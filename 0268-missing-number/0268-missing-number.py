class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        current =0
        for num in nums:
            if num != current:
                return current
            current+=1
        else:
            return num+1