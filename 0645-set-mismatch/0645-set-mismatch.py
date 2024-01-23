class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 1
        j = 0
        nums.sort()
        while i<len(nums):
            if nums[i] == nums[j]:
                first = nums.pop(j)
                break
            j=i
            i+=1
            
        i = 1
        j = 0
        while j<len(nums) and i == nums[j]:
            j=i
            i+=1
            
        return [first, i]