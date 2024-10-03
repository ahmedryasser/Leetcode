class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        vals = {}
        for num in nums:
            vals[num] = vals.get(num,0)+1
        for val in vals.values():
            if val%2 != 0:
                return False
        return True