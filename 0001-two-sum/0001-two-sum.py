class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i in range(len(nums)):
            comp = target-nums[i]
            if comp in numbers:
                return [i,numbers[comp]]
            numbers[nums[i]]=i
            
        
            