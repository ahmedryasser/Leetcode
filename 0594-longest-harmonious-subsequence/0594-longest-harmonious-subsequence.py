class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # nums.sort()
        vals = {}
        for num in nums:
            vals[num] = vals.get(num, 0) + 1
        result = 0
        for val, cnt in vals.items():
            if val+1 in vals:
                num = cnt + vals[val+1]
                result = max(result,num)
        return result