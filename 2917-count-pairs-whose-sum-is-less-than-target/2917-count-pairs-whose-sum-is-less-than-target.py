class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        count = 0
        vals = []
        for num in nums:
            for val in vals:
                if (val +num) < target:
                    count+=1
            vals.append(num)
        return count

