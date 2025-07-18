class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for n,num in enumerate(nums):
            if target-num in vals:
                print(vals)
                return [vals[target-num],n]
            vals[num] = n
            
        return -1
            